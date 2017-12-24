import json

data = json.load(open('data/NavDatav2.json', 'r'))

for record in data:
    print(record)
