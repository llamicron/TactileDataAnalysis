"""
Usage:
    cli.py skippers <time_interval> <skip_amount> [<format>]
    cli.py --version
    cli.py (-h | --help)

Options:
    -h --help          Show this screen
    -v --version       Show version.
    <time_interval>    Max time from the first skip to the last
    <skip_amount>      Amount of skips needed to qualify
    <format>           (json|guid(default)|html)
                        json - prints to terminal in a semi-readable way
                        guid - only prints the guids (default) to the terminal
                        html - Starts a webserver to show the results


"""

VERSION = 'v1.0.2'

import json

from docopt import docopt
from skippers import mark_skippers
from coolered import color


def entry(args):
    if args['--version']:
        print("Tactile TTS Data Analysis", end='')
        color('green', VERSION)
        print("David Sweeney & Luke Sweeney")
        return VERSION

    if args['skippers']:
        time = int(args['<time_interval>'])
        skip = int(args['<skip_amount>'])

        data = mark_skippers(time, skip)
        skippers = []
        for record in data:
            if record['skipper']:
                skippers.append(record)

        print(len(data), "records")
        print(len(skippers), "skippers")
        if args['<format>'] == 'write':
            with open('data/Skippers.json', 'w') as fi:
                print("Writing to Skippers.json")
                fi.write(json.dumps(data))
        return data

if __name__ == '__main__':
    entry(docopt(__doc__))
