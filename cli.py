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

VERSION = 'v0.0.1'

import json

from docopt import docopt
from improved_skippers import identify_skippers, write_skippers
from coolered import color

import sys
import os

def entry(args):
    if args['--version']:
        print("Tactile TTS Data Analysis", end='')
        color('green', VERSION)
        print("David Sweeney & Luke Sweeney")
        return VERSION

    if args['skippers']:
        time = int(args['<time_interval>'])
        skip = int(args['<skip_amount>'])

        skippers = identify_skippers(time, skip)

        if args['<format>'] == 'write':
            write_skippers(skippers)
        elif args['<format>'] == 'json':
            print(json.dumps(skippers))
        elif args['<format>'] == 'html':
            # identify_skippers(time, skip, write_to_file='static/skippers_for_web.json')
            from app import app
            color('green', "Web server running: visit http://localhost:5000/")
            app.run()
        else:
            for skipper in skippers:
                print(skipper['guid'])
            print(len(skippers))
            for skipper in skippers:
                assert skipper['skipper'] == 0 or skipper['skipper'] == 1
        return skippers

if __name__ == '__main__':
    entry(docopt(__doc__))
