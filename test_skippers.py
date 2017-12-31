"""
Run skippers.py first (with -w) and then run these tests.
"""

import unittest
import json
try:
    from pytest import main
except ImportError:
    from unittest import main

from skippers import indentify_skippers, time_interval, skip_amount

data = json.load(open('data/CountedNavData.json', 'r'))

class TestSkippers(unittest.TestCase):

    def test_interval_5_skip_amount_5(self):
        data = indentify_skippers(5, 5)
        skipper_guids = [
            "BE4CA75D-6FDD-44AC-B10D-EDD36CF404F8",
            "89D589AC-D35B-4524-8707-15194794827C",
            "A74ADC95-4FBE-4067-A9C5-6B8F7CEF5DEB",
            "1C5875D6-4C66-46E1-BF13-734821BE9A35",
            "E6C0F7B2-FB0F-4CC4-9654-6554276E2FEB",
            "4CAA20BE-77B7-4B45-8629-F1E3AFF98D66",
            "A8074511-0CDE-402B-B117-44D267F5DEC1",
            "A8074511-0CDE-402B-B117-44D267F5DEC1",
            "895C556E-EA3E-474F-896E-4BCF1834ABC8",
            "3A72DDFE-7FA8-42D3-9EA3-37D1B8410E7B",
            "D292784D-0463-413F-BA34-F94121FA453A",
            "42E2F2E5-62EF-417D-AE5A-FB7FE292A027",
            "05092872-9C7B-4B3F-9A49-16481DB05B1E",
            "0724F1CB-FE91-4F49-AF3B-840AB3C17862",
            "B7464B53-88D0-4B8A-AC1E-0F2B5335CAD7",
            "F849A99C-397F-4D8A-BDD4-D820C55A570D",
            "0D89E41D-A788-4F1A-8FB6-A5CCBC1FA868",
            "C96D62ED-FB49-4685-A5D6-A4F1E786D911",
            "FC42ED5E-D7AB-498A-99C2-DCEC30DF88C5",
            "4285FE84-B20B-4C61-B02A-53BCBD86CAB0",
            "686B6CB9-2E7D-49F6-A44A-E48F4480324D",
            "0F4DC3B2-9D67-4886-91D6-2383939E8520"
        ]
        for record in data:
            if record['guid'] in skipper_guids:
                assert record['skipper']
            else:
                assert not record['skipper']

    def test_interval_10_skip_amount_10(self):
        data = indentify_skippers(10, 10)
        skipper_guids = [
            "BE4CA75D-6FDD-44AC-B10D-EDD36CF404F8",
            "89D589AC-D35B-4524-8707-15194794827C",
            "A74ADC95-4FBE-4067-A9C5-6B8F7CEF5DEB",
            "1C5875D6-4C66-46E1-BF13-734821BE9A35",
            "E6C0F7B2-FB0F-4CC4-9654-6554276E2FEB",
            "4CAA20BE-77B7-4B45-8629-F1E3AFF98D66",
            "A8074511-0CDE-402B-B117-44D267F5DEC1",
            "A8074511-0CDE-402B-B117-44D267F5DEC1",
            "895C556E-EA3E-474F-896E-4BCF1834ABC8",
            "3A72DDFE-7FA8-42D3-9EA3-37D1B8410E7B",
            "D292784D-0463-413F-BA34-F94121FA453A",
            "42E2F2E5-62EF-417D-AE5A-FB7FE292A027",
            "05092872-9C7B-4B3F-9A49-16481DB05B1E",
            "0724F1CB-FE91-4F49-AF3B-840AB3C17862",
            "B7464B53-88D0-4B8A-AC1E-0F2B5335CAD7",
            "F849A99C-397F-4D8A-BDD4-D820C55A570D",
            "0D89E41D-A788-4F1A-8FB6-A5CCBC1FA868",
            "FC42ED5E-D7AB-498A-99C2-DCEC30DF88C5",
            "686B6CB9-2E7D-49F6-A44A-E48F4480324D",
            "0F4DC3B2-9D67-4886-91D6-2383939E8520"
        ]
        for record in data:
            if record['guid'] in skipper_guids:
                assert record['skipper']
            else:
                assert not record['skipper']


if __name__ == '__main__':
    main()
