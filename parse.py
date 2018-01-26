"""
Usage:
    parse <input_file> <output_file>
"""
import re
import sys
import json
import os

from docopt import docopt

class FileNotFound(Exception):
    pass

def chunk(list, interval):
    chunked_list = []
    for i in range(0, len(list), interval):
        chunked_list.append(list[i:i + interval])

    for action in chunked_list:
        if not len(action) == interval:
            raise ValueError("Not enough values to complete a chunk!")
    return chunked_list

def to_json(input_file):
    """
    Parses file (.dat) to json
    """
    if not os.path.isfile(input_file):
        raise FileNotFound("Couldn't find that file")
    lines = open(input_file, 'r').read().split('\n')
    data = []
    for line in lines:
        match = re.match(r'(.+)(.+\[.+\])', line)
        if match:
            guid = match.group(1).replace('\t', '')
            result_string = match.group(2)
            for ch in ['"', "'", '[', ']', '\t']:
                result_string = result_string.replace(ch, '')
            results = result_string.split(',')
            results = chunk(results, 3)
            for i in range(len(results)):
                results[i] = {
                    'action': results[i][0],
                    'location': results[i][1],
                    'time': results[i][2]
                }
            data.append({
                'guid': guid,
                'actions': results
            })
    return data

if __name__ == '__main__':
    args = docopt(__doc__)
    if os.path.isfile(args['<output_file>']):
        while True:
            choice = input(args['<output_file>'] + ' is already a file. Overwrite? ')
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
