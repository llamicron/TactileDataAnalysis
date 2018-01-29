"""
Usage:
    prepare.py <input_file>

Help:
    Replaces &quot; with a single quote character (')
    This will overwrite the input file with the fixed file.
"""

import os
import sys

from docopt import docopt
from custom_exceptions import FileNotFound

def prepare(input_file):
    if not os.path.isfile(input_file):
        raise FileNotFound("Couldn't find file: " + input_file)

    lines = []
    with open(input_file, 'r') as infile:
        for line in infile:
            lines.append(line.replace('&quot;', '\''))

    with open(input_file, 'w') as outfile:
        for line in lines:
            outfile.write(line)

if __name__ == '__main__':
    args = docopt(__doc__)
    data = prepare(args['<input_file>'])
