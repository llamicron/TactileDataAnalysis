import json
import sys

# Chnage this with the CLI
time_interval = 10
skip_amount = 10


def identify_skippers(time_interval, skip_amount, write_to_file=False):
    skipper_count = 0
    data = json.load(open('data/CountedNavData.json', 'r'))
    skippers = []
    for record in data:
        skipper = False
        # Order by time
        record['actions'] = sorted(record['actions'], key=lambda k: k['time'])
        # Find string of F or FP
        forwards = [x for x in record['actions']
                    if x['action'] == "FP" or x['action'] == "F"]
        if not forwards:
            skipper = False
            # continue

        # If found, check if first and last are within time frame
        for i in range(len(forwards) - skip_amount):
            if float(forwards[i + skip_amount]['time']) - float(forwards[i]['time']) <= time_interval:
                skipper = True
        if skipper:
            record['skipper'] = skipper
            skippers.append(record)
    if write_to_file:
        with open(write_to_file, 'w') as f:
            f.write(json.dumps(skippers))
    return skippers

if '-w' in sys.argv:
    print("Writing file")
    data = identify_skippers(time_interval, skip_amount)


if '-p' in sys.argv:
    data = identify_skippers(time_interval, skip_amount)
    print(data)
