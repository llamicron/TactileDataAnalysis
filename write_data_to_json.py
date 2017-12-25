"""
Run this script with '-w' to write to data/NavData.json
Otherwise it will exit doing with the parsed data
"""

import re
import sys
import json

def chunk(list, interval):
    chunked_list = []
    for i in range(0, len(list), interval):
        chunked_list.append(list[i:i + interval])

    for action in chunked_list:
        if not len(action) == interval:
            raise ValueError("Not enough values to complete a chunk!")
    return chunked_list


lines = open('data/NavData.dat', 'r').read().split('\n')
data = []

for line in lines:
    match = re.match(r'(.+)(.+\[.+\])', line)
    if match:
        guid = match.group(1)
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

if '-w' in sys.argv:
    print("Writing to file")
    with open('data/NavData.json', 'w') as f:
        f.write(json.dumps(data))
