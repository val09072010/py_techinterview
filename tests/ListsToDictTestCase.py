#!/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import os
import unittest
import o1_listconvertor.ListsToDictConvertersFunc as Tested
from o1_listconvertor.ListsToDictConvertersClass import ManualListsConverter as ZipLC, MapListsConverter as ItertoolLC
from o1_listconvertor.ListsToDictConvertorsDecorator import lists_to_dict_itertools, lists_to_dict_manual_zip
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class ListsToDictTestCase(unittest.TestCase):
    keys_longer_map = dict({(1, 'one'), (2, 'two'), (3, 'three'), (4, None)})
    lists_eq_map = dict({(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')})
    values_longer_map = dict({(1, 'one'), (2, 'two'), (3, 'three')})

    long_keys = [1, 2, 3, 4]
    short_keys = [1, 2, 3]
    short_values = ['one', 'two', 'three']
    long_values = ['one', 'two', 'three', 'four']

    zzip = None
    iiter = None

    def setUp(self):
        self.zzip = ZipLC()
        self.iiter = ItertoolLC()

    def tearDown(self):
        self.zzip = None
        self.iiter = None

    def test_keys_longer_than_vals(self):
        self.assertEqual(self.keys_longer_map, Tested.lists_to_dict_manual_zip(self.long_keys, self.short_values))
        self.assertEqual(self.keys_longer_map, Tested.lists_to_dict_itertools(self.long_keys, self.short_values))
        self.assertEqual(self.keys_longer_map, self.zzip.lists_to_dict(self.long_keys, self.short_values))
        self.assertEqual(self.keys_longer_map, self.iiter.lists_to_dict(self.long_keys, self.short_values))
        self.assertEqual(self.keys_longer_map, lists_to_dict_manual_zip(self.long_keys, self.short_values))
        self.assertEqual(self.keys_longer_map, lists_to_dict_itertools(self.long_keys, self.short_values))

    def test_keys_equal_to_vals(self):
        self.assertEqual(self.lists_eq_map, Tested.lists_to_dict_manual_zip(self.long_keys, self.long_values))
        self.assertEqual(self.lists_eq_map, Tested.lists_to_dict_itertools(self.long_keys, self.long_values))
        self.assertEqual(self.lists_eq_map, self.zzip.lists_to_dict(self.long_keys, self.long_values))
        self.assertEqual(self.lists_eq_map, self.iiter.lists_to_dict(self.long_keys, self.long_values))
        self.assertEqual(self.lists_eq_map, lists_to_dict_manual_zip(self.long_keys, self.long_values))
        self.assertEqual(self.lists_eq_map, lists_to_dict_itertools(self.long_keys, self.long_values))

    def test_keys_shorter_than_vals(self):
        self.assertEqual(self.values_longer_map, Tested.lists_to_dict_manual_zip(self.short_keys, self.long_values))
        self.assertEqual(self.values_longer_map, Tested.lists_to_dict_itertools(self.short_keys, self.long_values))
        self.assertEqual(self.values_longer_map, self.zzip.lists_to_dict(self.short_keys, self.long_values))
        self.assertEqual(self.values_longer_map, self.iiter.lists_to_dict(self.short_keys, self.long_values))
        self.assertEqual(self.values_longer_map, lists_to_dict_manual_zip(self.short_keys, self.long_values))
        self.assertEqual(self.values_longer_map, lists_to_dict_itertools(self.short_keys, self.long_values))


if __name__ == '__main__':
    unittest.main()
