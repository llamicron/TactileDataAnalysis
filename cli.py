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
from skippers import indentify_skippers
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
        if not 0 < time <= 60:
            raise ValueError("time_interval should be between 1 and 60")
        if not 0 < skip <= 60:
            raise ValueError("skip_amount should be between 1 and 60")

        skippers = indentify_skippers(time, skip)

        if args['<format>'] == 'json':
            print(json.dumps(skippers))
        elif args['<format>'] == 'html':
            # indentify_skippers(time, skip, write_to_file='static/skippers_for_web.json')
            import web
            color('green', "Web server running: visit http://localhost:5000/")
            web.app.run()

        else:
            for skipper in skippers:
                print(skipper['guid'])
        print(len(skippers), "skippers")
        return skippers

if __name__ == '__main__':
    entry(docopt(__doc__))
