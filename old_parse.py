"""
This module is for parsing strings created by TactileTTS.
Data is in data/TactileTTS_Phase_2.csv
"""

import csv
import sys

def chunk(list, interval):
    chunked_list = []
    for i in range(0, len(list), interval):
        chunked_list.append(list[i:i + interval])

    for action in chunked_list:
        if not len(action) == interval:
            raise ValueError("Not enough values to complete a chunk!")
    return chunked_list

def key_actions(actions):
    keyed_actions = []

    if not actions[0]:
        return []

    for item in chunk(actions, 3):
        keyed_actions.append({
            'action': item[0],
            'location': item[1],
            'time': item[2]
        })
    return keyed_actions

def split_action_string(action_string):
    actions = action_string.split(',')
    for ch in ['[', ']', "'", '"', ' ']:
        actions = [x.replace(ch, '') for x in actions]
    return actions

def get_list_from_action_string(action_string):
    actions = split_action_string(action_string)
    return chunk(actions, 3)

def get_guid(action_string):
    actions = split_action_string(action_string)
    return actions[-2]

def get_group(action_string):
    actions = split_action_string(action_string)
    return int(actions[-1])

def action_list(action_string):
    actions = get_list_from_action_string(action_string)
    keyed_actions = key_actions(actions)
    return keyed_actions

def from_csv(file):
    data = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def list_to_dict(data):
    sorted_data = {}
    for item in data:
        guid = get_guid()
        sys.exit(1)
    return sorted_data
