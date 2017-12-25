import json
import sys

# Chnage this with the CLI
time_interval = 500
skip_amount = 0

data = json.load(open('data/CountedNavData.json', 'r'))

skipper_count = 0

# for record in data:
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

if '-w' in sys.argv:
    print("Writing file")
    with open('data/Skippers.json', 'w') as f:
        f.write(json.dumps(data))
print("Amount of skippers: " + str(skipper_count))

# TODO: Write a unittest for skippers
