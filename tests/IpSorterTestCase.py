#!/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import os
import unittest
import o2_ipsorter.ip_sorter as tested
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class IpSorterTestCase(unittest.TestCase):
    test_file = "./access.test"
    wrong_ip = "192.168.0.1"

    def test_right_ips(self):
        ip_map = tested.ip_collector(self.test_file)
        self.assertFalse(self.wrong_ip in ip_map.keys())
        self.assertEqual(2, len(ip_map.keys()))

    def test_sorting_is_ok(self):
        ip_map = tested.ip_collector(self.test_file)
        ip_sorted = tested.ip_sorter(ip_map)
        ip1, num1 = ip_sorted[0]
        ip2, num2 = ip_sorted[1]
        self.assertTrue(num1 > num2)


if __name__ == '__main__':
    unittest.main()
