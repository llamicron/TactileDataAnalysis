# TactileTTS Data Analysis
## Proccess
Each module in the proccess (`parse.py`, `count.py`, `skippers.py`, `export.py`, in that order) has a CLI. Run it like this:
```
$ python parse.py --help
$ python count.py --help
...
```

This will show you the help page. Each module takes an input file and an output file. `skippers.py` takes 2 extra arguments, the amount of skips needed (`skip_amount`) and the time frame for those skips (`time_interval`).

See the help page on each module to see the recommended files to read from and write to, but you can use any file.

**It's important that you run the 4 steps in the right order.**

1. `parse.py`
2. `count.py`
3. `skippers.py`
4. `export.py`

Don't use `cli.py` anymore

#
### `parse.py`
Reads from a tab delimited file (eg. `NavData.dat`) and converts it to json. Writes to a json file (eg. `NavData.json`)

### `count.py`
Reads from the output file of `parse.py` (eg. `NavData.json`) and counts the number of actions + training actions for each user. This will be added on to the json object under the `count` field. Write to another json file (eg. `CountedNavData.json`)

### `skippers.py`
Reads from the output file of `count.py` (eg. `CountedNavData.json`) and marks all found skippers. Write to another json file (eg. `Skippers.json`)

Takes 2 additional arguments: `skip_amount` and `time_interval`

A skipper is a user who navigates forward (`F` or `FP`) `skip_amount` times in `time_interval` seconds.

### `export.py`
Reads from output file of `skippers.py` (eg. `Skippers.json`) and converts output to CSV. Write to a CSV file (eg. `NavData.csv`)

#
All file names can be changed

**Reminder:** be sure to add `data/` to the beginning of the files you read and write from. Kepp data files in the `data/` directory.
