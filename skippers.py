import json
import sys

# Chnage this with the CLI
time_interval = 10
skip_amount = 10


def indentify_skippers(time_interval, skip_amount):
    skipper_count = 0
    data = json.load(open('data/CountedNavData.json', 'r'))
    for x in range(len(data)):
        record = data[x]
        skipper = False
        # Order by time
        record['actions'] = sorted(record['actions'], key=lambda k: k['time'])
        # Find string of F or FP
        forwards = [x for x in record['actions'] if x['action'] == "FP" or x['action'] == "F"]
        if not forwards:
            skipper = False
            # continue

        # If found, check if first and last are within time frame
        for i in range(len(forwards) - skip_amount):
            if float(forwards[i + skip_amount]['time']) - float(forwards[i]['time']) <= time_interval:
                skipper = True
        if skipper:
            skipper_count += 1
        data[x]['skipper'] = skipper
        # print("Number of skippers: " + skipper_count)
    return data

if '-w' in sys.argv:
    print("Writing file")
    data = indentify_skippers(time_interval, skip_amount)
    with open('data/Skippers.json', 'w') as f:
        f.write(json.dumps(data))

if '-p' in sys.argv:
    data = indentify_skippers(time_interval, skip_amount)
    print(data)
