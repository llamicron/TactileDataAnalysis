"""
Usage:
    all.py <input_file> <skip_amount> <time_interval>

Details:
    This runs all the steps, in order.
    Put your starting file (tab delimited, probably from excel) in data/[DATE]

Example:
    $ python all.py data/2018_01_29/NavData.dat 6 5
"""

# 1. prepare
# 2. parse
# 3. count
# 4. skippers
# 5. export

import os

from docopt import docopt


import prepare
import parse
import count
import skippers
import export # lol

from custom_exceptions import FileNotFound

if __name__ == '__main__':
    args = docopt(__doc__)
    fi = args['<input_file>']
    # path, fi = os.path.split(args['<input_file>'])
    prepare.prepare(fi)
    parsed = parse.to_json(open(fi, 'r').read().split('\n'))
    counted = count.to_json(parsed)
    marked = skippers.mark_skippers(counted, args['<skip_amount>'], args['<time_interval>'])
    to_export = export.export(marked)
    exported_filename = fi.split('.')[0] + '.csv'
    assert not os.path.isfile(exported_filename)
    export.write_csv(exported_filename, to_export)
    print('Done')


