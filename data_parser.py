from pprint import pprint

import parse_methods as parse

# Get data from csv file
data = parse.from_csv('data/TactileTTS_Phase_2.csv')

# The first row is a key, not needed
del data[0]

# Force into dict
data = parse.list_to_dict(data)
# print(data)
