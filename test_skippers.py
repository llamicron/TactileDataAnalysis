import unittest
import json

data = json.load(open('data/NavData.json', 'r'))

class TestSkippers(unittest.TestCase):
    def setUp(self):
        self.record = data[0]

    def test_the_fleeble(self):
        print(self.record)
