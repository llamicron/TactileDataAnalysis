"""
Usage:
    count.py <input_file> <output_file>
"""

import json
import sys
import os
from custom_exceptions import FileNotFound

from docopt import docopt

# From 'data/NavData.json' to 'data/CountedNavData.json', normally

def to_json(input_file):
    if not os.path.isfile(input_file):
        FileNotFound("Couldn't find file: " + input_file)
    data = json.load(open(input_file, 'r'))

    for record in data:
        count = {
            'training_actions': 0,
            'actions': 0,
            'BG': 0,
            'FG': 0,
        }
        for action in record['actions']:
            if 'BG' in action['action']:
                count['BG'] += 1

            if 'FG' in action['action']:
                count['FG'] += 1

            if int(action['location']) == 0:
                count['training_actions'] += 1
        count['actions'] = len(record['actions']) - (count['BG'] + count['FG'])
        record['count'] = count
    return data

if '-w' in sys.argv:
    print("Writing to file: data/CountedNavData.json")
    with open('data/CountedNavData.json', 'w') as f:
        f.write(json.dumps(data))

if __name__ == '__main__':
    args = docopt(__doc__)
    if os.path.isfile(args['<output_file>']):
        while True:
            choice = input(args['<output_file>'] +
                           ' is already a file. Overwrite? ')
            if choice.upper() == 'Y':
                break
            elif choice.upper() == 'N':
                print('Quiting')
                sys.exit(0)
            else:
                print('Invalid choice, type y or n')
    print('Writing')
    data = to_json(args['<input_file>'])
    with open(args['<output_file>'], 'w') as f:
        f.write(json.dumps(data))
