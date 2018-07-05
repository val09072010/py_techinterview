#!/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import os
import unittest
import o1_listconvertor.ListsToDictConvertersFunc as Tested
from o1_listconvertor.ListsToDictConvertersClass import ManualListsConverter as ZipLC, MapListsConverter as ItertoolLC
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class ListsoDictTestCase(unittest.TestCase):
    keys_longer_map = dict({(1, 'one'), (2, 'two'), (3, 'three'), (4, None)})
    lists_eq_map = dict({(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')})
    values_longer_map = dict({(1, 'one'), (2, 'two'), (3, 'three')})

    keys4 = [1, 2, 3, 4]
    keys3 = [1, 2, 3]
    values3 = ['one', 'two', 'three']
    values4 = ['one', 'two', 'three', 'four']

    zzip = None
    iiter = None

    def setUp(self):
        self.zzip = ZipLC()
        self.iiter = ItertoolLC()

    def tearDown(self):
        self.zzip = None
        self.iiter = None

    def test_keys_longer_than_vals_functions(self):
        self.assertEqual(self.keys_longer_map, Tested.lists_to_dict_manual_zip(self.keys4, self.values3))
        self.assertEqual(self.keys_longer_map, Tested.lists_to_dict_itertools(self.keys4, self.values3))
        self.assertEqual(self.keys_longer_map, self.zzip.lists_to_dict(self.keys4, self.values3))
        self.assertEqual(self.keys_longer_map, self.iiter.lists_to_dict(self.keys4, self.values3))

    def test_keys_equal_to_vals_functions(self):
        self.assertEqual(self.lists_eq_map, Tested.lists_to_dict_manual_zip(self.keys4, self.values4))
        self.assertEqual(self.lists_eq_map, Tested.lists_to_dict_itertools(self.keys4, self.values4))
        self.assertEqual(self.lists_eq_map, self.zzip.lists_to_dict(self.keys4, self.values4))
        self.assertEqual(self.lists_eq_map, self.iiter.lists_to_dict(self.keys4, self.values4))

    def test_keys_shorter_than_vals_functions(self):
        self.assertEqual(self.values_longer_map, Tested.lists_to_dict_manual_zip(self.keys3, self.values4))
        self.assertEqual(self.values_longer_map, Tested.lists_to_dict_itertools(self.keys3, self.values4))
        self.assertEqual(self.values_longer_map, self.zzip.lists_to_dict(self.keys3, self.values4))
        self.assertEqual(self.values_longer_map, self.iiter.lists_to_dict(self.keys3, self.values4))


if __name__ == '__main__':
    unittest.main()
