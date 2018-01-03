import json
import sys

def identify_skippers():
    guids = []
    data = json.load(open('data/CountedNavData.json', 'r'))
    assert data

    for record in data:

        if '0F2B5335CAD7' not in record['guid']:
            continue

        actions = record['actions']
        assert isinstance(actions, list)
        # Cast times to float
        for i in range(len(actions)):
            actions[i]['time'] = float(actions[i]['time'])
        # Sort actions by time
        actions.sort(key=lambda x: x['time'])
        assert isinstance(actions[0]['time'], float)
        for i in range(1, len(actions)):
            time = actions[i]['time']
            prev = actions[i - 1]['time']
            assert time > prev

        skip_amount = 0
        time_diff = 0
        prev_time = 0
        for i in range(len(actions)):
            action = actions[i]
            action['time'] = float(action['time'])
            if action['location'] == '0':
                continue
            if action['time'] == float(actions[i - 1]['time']):
                continue

            # (i + 1) != len(actions)
            if action['action'] == 'F' or action['action'] == 'FP' and (i + 1) != len(actions):
                print('inc @' + str(i))
                skip_amount += 1
                prev_time = actions[i - 1]['time']
            else:
                if skip_amount >= 4:
                    if record['guid'] not in guids:
                        guids.append(record['guid'])
                    for guid in guids:
                        print(guid)
                    print(len(guids))
                    for guid in guids:
                        print(guid)
                    print(len(guids))

                # print("GUID: ", end='')
                # print(record['guid'][-6:])
                # print('Time Diff: ', end='')
                # print(time_diff)
                # print('Prev Time: ', end='')
                # print(prev_time)
                # print('Skip Amount: ', end='')
                # print(skip_amount)
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
