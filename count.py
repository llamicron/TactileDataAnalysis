import json
import sys

data = json.load(open('data/NavData.json', 'r'))

for record in data:
    count = {
        'training_actions': 0,
        'actions': 0,
        'BG': 0,
        'FG': 0,
    }
    for action in record['results']:
        if 'BG' in action['action']:
            count['BG'] += 1

        if 'FG' in action['action']:
            count['FG'] += 1

        if int(action['location']) == 0:
            count['training_actions'] += 1
    count['actions'] = len(record['results']) - (count['BG'] + count['FG'])
    record['count'] = count


if '-w' in sys.argv:
    print("Writing to file: data/CountedNavData.json")
    with open('data/CountedNavData.json', 'w') as f:
        f.write(json.dumps(data, indent=2))
