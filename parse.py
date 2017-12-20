# Get the full string
# split into action_string, guid, group
# Turn into dict

import csv
import sys
import re

def from_csv(file):
    data = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def get_guid(full_string):
    return full_string.split(',')[-2]

def get_group(full_string):
    return int(full_string.split(',')[-1])

def get_action_string(full_string):
    regex = '\[(.+)\]'
    result = re.search(regex, full_string).group(0)

    for ch in ['[', ']']:
        result = result.replace(ch, '')
    return result

def chunk(list, interval):
    chunked_list = []
    for i in range(0, len(list), interval):
        chunked_list.append(list[i:i + interval])

    for action in chunked_list:
        if not len(action) == interval:
            raise ValueError("Not enough values to complete a chunk!")
    return chunked_list

def get_actions(action_string):
    actions = action_string.split(',')
    for i in range(len(actions)):
        for ch in ['"', "'", ' ']:
            actions[i] = actions[i].replace(ch, '')
    return chunk(actions, 3)

def actions_to_dict(actions):
    mapped_actions = []
    for action in actions:
        mapped_actions.append({
            'action': action[0],
            'location': int(action[1]),
            'time': float(action[2])
        })
    return mapped_actions

def to_dict(guid, group, actions):
    return {
        'guid': guid,
        'group': group,
        'actions': actions_to_dict(actions)
    }
