"""
if there are 6 or more consecutive forward navigations within a 4 second period

forwards == 'FP' or 'F'

find strings of consecutive forwards
find time diff between forward at i and forward at i + 6
if time diff < 4 seconds, it's a skipper
"""

import json
from contextlib import suppress
import sys

target_set = [
    '1C5875D6-4C66-46E1-BF13-734821BE9A35',
    'BE4CA75D-6FDD-44AC-B10D-EDD36CF404F8',
    '0D89E41D-A788-4F1A-8FB6-A5CCBC1FA868',
    'D292784D-0463-413F-BA34-F94121FA453A',
    'C96D62ED-FB49-4685-A5D6-A4F1E786D911',
    'FC42ED5E-D7AB-498A-99C2-DCEC30DF88C5',
    '42E2F2E5-62EF-417D-AE5A-FB7FE292A027',
    'D36436E3-2399-4817-B863-D3742C691F7E',
    '89D589AC-D35B-4524-8707-15194794827C',
    '05092872-9C7B-4B3F-9A49-16481DB05B1E',
    '0724F1CB-FE91-4F49-AF3B-840AB3C17862',
    'B7464B53-88D0-4B8A-AC1E-0F2B5335CAD7',
    'E6C0F7B2-FB0F-4CC4-9654-6554276E2FEB',
    '4285FE84-B20B-4C61-B02A-53BCBD86CAB0',
    'A74ADC95-4FBE-4067-A9C5-6B8F7CEF5DEB',
    '4CAA20BE-77B7-4B45-8629-F1E3AFF98D66',
    '686B6CB9-2E7D-49F6-A44A-E48F4480324D',
    'F849A99C-397F-4D8A-BDD4-D820C55A570D',
    'A8074511-0CDE-402B-B117-44D267F5DEC1',
    '895C556E-EA3E-474F-896E-4BCF1834ABC8',
    '3A72DDFE-7FA8-42D3-9EA3-37D1B8410E7B'
]

def dd(var_list=False):
    with suppress(ImportError):
        import sys
    if var_list:
        print(str(var_list))
    print('exiting')
    sys.exit(0)

def cast_times_to_float(actions):
    for i in range(len(actions)):
        actions[i]['time'] = float(actions[i]['time'])
        assert type(actions[i]['time']) is float
    return actions

def is_forward(action):
    if action['action'] == 'FP' or action['action'] == 'F':
        return True
    return False

def find_consecutive_forward_groups(actions, min_size = 0):
    forwards = []
    chunk = []
    for i in range(len(actions)):
        action = actions[i]
        if is_forward(action):
            chunk.append(action)

        # If this is the last iteration or it's not a forward (ending the streak)
        if not is_forward(action) or i + 1 == len(actions):
            if len(chunk) >= min_size:
                forwards.append(chunk)
                chunk = []
    return forwards

def mark_skippers(skip_amount, time_interval):
    data = json.load(open('data/CountedNavData.json', 'r'))
    assert data

    marked = []

    for record in data:
        """
        returns the full data set with skippers marked ie. record['skipper'] == True
        """
        actions = record['actions']
        record['skipper'] = 0

        actions = cast_times_to_float(actions)

        # Sort actions by time
        actions.sort(key=lambda x: x['time'])

        forwards = find_consecutive_forward_groups(actions, min_size = int(skip_amount))
        for chunk in forwards:
            # a 'chunk' is a group of consecutive forwards
            # If there is a string of skip_amount size, where the time diff is less than time_interval, it's a skipper
            # get time diff on string of forwards of size skip_amount
            for i in range(len(chunk) - skip_amount):
                time_diff = chunk[i + skip_amount]['time'] - chunk[i]['time']
                if time_diff <= time_interval:
                    record['skipper'] = 1
        marked.append(record)
    return marked

if __name__ == '__main__':

    if 'guids' in sys.argv:
        data = mark_skippers(6, 4)
        skipper_guids = []
        for record in data:
            if record['skipper']:
                skipper_guids.append(record['guid'])
        print(skipper_guids)
        print(len(skipper_guids))

    if 'write' in sys.argv:
        with open('data/Skippers.json', 'w') as f:
            print("Writing to Skippers.json")
            f.write(json.dumps(mark_skippers(6, 5)))

    if 'test' in sys.argv:
        found = False
        # 6, 4
        for x in range(1, 11):
            for y in range(1, 11):
                data = mark_skippers(x, y)
                guids = []
                for record in data:
                    if bool(record['skipper']):
                        guids.append(record['guid'])
                if sorted(guids) == sorted(target_set):
                    print(guids)
                    print(len(guids))
                    found = True
                    print("Target set found at x =", x, ", y =", y)
        if not found:
            print("No data sets match target set")


