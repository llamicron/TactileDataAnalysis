import unittest
import pytest

import parse

class TestParser(unittest.TestCase):
    def setUp(self):
        self.RAW_DATA = parse.from_csv('data/TactileTTS_Phase_2.csv')
        self.full_string = "\"['TF,0,1493756240.20148', 'TF,0,1493756242.20148', 'TF,0,1493756244.20348']\",91ED2E05-7A39-4249-8504-0DDB64E5E27F,2"

    def test_raw_data(self):
        assert len(self.RAW_DATA) >= 75
        assert isinstance(self.RAW_DATA, list)

    def test_get_action_string(self):
        action_string = parse.get_action_string(self.full_string)
        assert action_string == "'TF,0,1493756240.20148', 'TF,0,1493756242.20148', 'TF,0,1493756244.20348'"

    def test_get_guid(self):
        guid = parse.get_guid(self.full_string)
        assert guid == "91ED2E05-7A39-4249-8504-0DDB64E5E27F"

    def test_get_group(self):
        group = parse.get_group(self.full_string)
        assert group == 2

    def test_get_actions(self):
        actions = parse.get_actions(parse.get_action_string(self.full_string))
        assert len(actions) == 3
        for action in actions:
            assert len(action) == 3
        assert actions == [['TF', '0', '1493756240.20148'], ['TF', '0', '1493756242.20148'], ['TF', '0', '1493756244.20348']]

    def test_chunk(self):
        starting = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        interval = 3
        chunked = parse.chunk(starting, interval)
        assert len(chunked) == len(starting) / interval

        with self.assertRaises(ValueError):
            chunked = parse.chunk(starting[:7], interval)

    def test_to_dict(self):
        guid = parse.get_guid(self.full_string)
        group = parse.get_group(self.full_string)
        actions = parse.get_actions(parse.get_action_string(self.full_string))
        assert guid == "91ED2E05-7A39-4249-8504-0DDB64E5E27F"
        assert group == 2
        assert actions == [['TF', '0', '1493756240.20148'], ['TF', '0', '1493756242.20148'], ['TF', '0', '1493756244.20348']]

        record = parse.to_dict(guid, group, actions)
        assert isinstance(record, dict)

        assert record['guid'] == "91ED2E05-7A39-4249-8504-0DDB64E5E27F"
        assert record['group'] == 2
        assert record['actions'] == [{'action': 'TF', 'location': 0, 'time': 1493756240.20148}, {
            'action': 'TF', 'location': 0, 'time': 1493756242.20148}, {'action': 'TF', 'location': 0, 'time': 1493756244.20348}]
