import json
import csv

def export():
    data = json.load(open('data/Skippers.json', 'r'))
    rows = []
    for record in data:
        new_format = {
            'participantGuid': record['guid'],
            'NavTotal': record['count']['actions'],
            'TrainTotal': record['count']['training_actions'],
            'BGFGTotal': (record['count']['BG'] + record['count']['FG']) / 2,
            'Skipper': int(record['skipper'])
        }

        rows.append(new_format)
    with open('data/NavData.csv', 'w') as f:
        w = csv.writer(f)
        w.writerow(rows[0].keys())
        for row in rows:
            w.writerow(row.values())

if __name__ == '__main__':
    export()
