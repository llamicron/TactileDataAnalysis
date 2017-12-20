import csv
import sys

def chunk(list, interval):
    chunked_list = []
    for i in range(0, len(list), interval):
        chunked_list.append(list[i:i + interval])

    for action in chunked_list:
        if not len(action) == 3:
            print(action)
            sys.exit(1)
    return chunked_list

def key_actions(actions):
    keyed_actions = []

    if not actions[0]:
        return []

    for item in chunk(actions, 3):
        try:
            keyed_actions.append({
                'action': item[0],
                'location': item[1],
                'time': item[2]
            })
        except IndexError:
            print("Item: ")
            print(type(item))
            print(item)
            print("---")
    return keyed_actions

def action_list(action_string):
    actions = action_string.split(',')
    for ch in ['[', ']', "'"]:
        actions = [x.replace(ch, '') for x in actions]

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
        sorted_data[item[1]] = {
            'actions': action_list(item[0]),
            'group': int(item[2])
        }
    return sorted_data
