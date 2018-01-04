import json
import sys

def identify_skippers(skip_amount, time_interval):
    marked = []
    data = json.load(open('data/CountedNavData.json', 'r'))
    assert data

    for record in data:
        actions = record['actions']
        record['skipper'] = 0
        # Test
        assert isinstance(actions, list)
        # Cast times to float
        for i in range(len(actions)):
            actions[i]['time'] = float(actions[i]['time'])
            # Test
            assert isinstance(actions[i]['time'], float)
        # Sort actions by time
        actions.sort(key=lambda x: x['time'])
        # Test
        for i in range(1, len(actions)):
            time = actions[i]['time']
            prev = actions[i - 1]['time']
            assert time > prev
        # End Test

        forwards = []
        for i in range(len(actions)):
            if actions[i]['action'] == 'F' or actions[i]['action'] == 'FP':
                forwards.append(i)
        temp = []
        chunks = []
        for item in forwards:
            if len(temp) > 0 and item == temp[-1] + 1:
                temp.append(item)
            else:
                temp = [item]
                chunks.append(temp)
        # This is no longer needed
        del forwards
        for forwards in chunks:
            if len(forwards) < skip_amount:
                continue
            # print(forwards)
            # for forward in forwards:
            time_diff = actions[forwards[-1]]['time'] - \
                actions[forwards[0]]['time']
            # time_diff and time_interval
            record['skipper'] = int(time_diff < time_interval)
            if record['skipper']:
                break
            # print(record['skipper'])
        marked.append(record)
    return marked

def write_skippers(data):
    with open('data/Skippers.json', 'w') as f:
        f.write(json.dumps(data))

if '-w' in sys.argv:
    data = identify_skippers(5, 10)
    write_skippers(data)

if __name__ == '__main__':
    data = identify_skippers(5, 10)
    print("5 and 10")
    for record in data:
        print(record['guid'][-6:])
