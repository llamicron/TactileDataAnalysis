import re
import json

def chunk(list, interval):
    chunked_list = []
    for i in range(0, len(list), interval):
        chunked_list.append(list[i:i + interval])

    for action in chunked_list:
        if not len(action) == interval:
            raise ValueError("Not enough values to complete a chunk!")
    return chunked_list


lines = open('data/NavDatav2.dat', 'r').read().split('\n')
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
        data.append({
            'guid': guid,
            'results': results
        })

