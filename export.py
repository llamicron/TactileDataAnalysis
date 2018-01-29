"""
Usage:
    export.py <input_file> <output_file>

Recommended:
    input_file: data/Skippers.json
    output_file: data/NavData.csv
"""
import json
import csv
import os
import sys

from docopt import docopt
from custom_exceptions import FileNotFound

def export(data):
    rows = []
    for record in data:
        new_format = {
            'participantGuid': record['guid'],
            'NavTotal': record['count']['actions'],
            'TrainTotal': record['count']['training_actions'],
            'BGFGTotal': (record['count']['BG'] + record['count']['FG']) / 2,
            'Skipper': int(record['skipper'])
        }

        rows.append(new_format)
    return rows

def write_csv(file, rows):
    with open(file, 'w') as f:
        w = csv.writer(f)
        w.writerow(rows[0].keys())
        for row in rows:
            w.writerow(row.values())

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
    rows = export(json.load(open(args['<input_file>'], 'r')))
    write_csv(args['<output_file>'], rows)

