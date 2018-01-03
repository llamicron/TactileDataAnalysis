import json
import sys

def identify_skippers():
    data = json.load(open('data/CountedNavData.json', 'r'))
    assert data

    for record in data:
        actions = record['actions']
        assert isinstance(actions, list)
        # Sort actions by time
        actions.sort(key=lambda x: x['time'])
        for i in range(len(actions)):
            this_time = actions[i]['time']
            prev_time = actions[i - 1]['time']
            print("Prev time: " + prev_time)
            print("This time: " + this_time)
        for action in actions:
            assert actions[0]['time'] < actions[-1]['time']


        skip_amount = 0
        for i in range(len(actions)):
            action = actions[i]
            action['time'] = float(action['time'])
            if action['location'] == '0':
                continue
            if action['time'] == float(actions[i - 1]['time']):
                continue
            if action['action'] == 'F' or action['action'] == 'FP':
                skip_amount += 1
                prev_time = actions[i - 1]['time']
            else:
                # Reset everything
                time_diff = 0
                prev_time = 0
                skip_amount = 0
                continue

            if skip_amount == 1:
                time_diff = 0
            else:
                time_diff += (action['time'] - prev_time)
            # print(record['guid'][-6:] + ": " + action['location'] + ": ", end='')
            # print(time_diff)






if __name__ == '__main__':
    identify_skippers()
