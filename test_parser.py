import unittest
import pytest

import parse

class TestParser(unittest.TestCase):
    def setUp(self):
        self.RAW_DATA = parse.from_csv('data/TactileTTS_Phase_2.csv')
        self.action_string = "\"['TF,0,1493756240.20148', 'TF,0,1493756242.20148', 'TF,0,1493756244.20348']\",91ED2E05-7A39-4249-8504-0DDB64E5E27F,2"

    def test_raw_data(self):
        assert len(self.RAW_DATA) >= 75
        assert isinstance(self.RAW_DATA, list)

    def test_chunk(self):
        starting = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        chunk_size = 3
        chunked = parse.chunk(starting, chunk_size)
        assert len(chunked) == len(starting) / chunk_size
        for chunk in chunked:
            assert len(chunk) == chunk_size

        with self.assertRaises(ValueError):
            del starting[0]
            parse.chunk(starting, chunk_size)

        assert parse.chunk([], 3) == []

    def test_split_action_string(self):
        action_list = parse.split_action_string(self.action_string)
        assert action_list == ['TF', '0', '1493756240.20148', 'TF', '0', '1493756242.20148',
                               'TF', '0', '1493756244.20348', '91ED2E05-7A39-4249-8504-0DDB64E5E27F', '2']

    def test_get_list_from_action_string(self):
        actions = parse.get_list_from_action_string(self.action_string)
        assert isinstance(actions, list)
        assert len(actions) == 3
        for action in actions:
            assert len(action) == 3
            assert 'TF' in action[0]
            assert action[1] == '0'
            assert '.' in action[2]

    def test_get_guid(self):
        assert parse.get_guid(self.action_string) == "91ED2E05-7A39-4249-8504-0DDB64E5E27F"

    def test_get_group(self):
        assert parse.get_group(self.action_string) == 2
