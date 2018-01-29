"""
Usage:
    count.py <input_file> <output_file>

Recommended:
    input_file: data/NavData.json
    output_file: data/CountedNavData.json
"""

import json
import sys
import os
from custom_exceptions import FileNotFound

from docopt import docopt

def to_json(data):
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
    data = to_json(json.load(open(args['<input_file>'], 'r')))
    with open(args['<output_file>'], 'w') as f:
        f.write(json.dumps(data))
