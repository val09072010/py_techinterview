#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import itertools


def lists_to_dict(inner):
    def decor(*args):
        values = args[1]
        keys = args[0]
        if len(keys) <= len(values):
            res = dict(zip(keys, values))
        else:
            res = inner(*args)
        return res
    return decor


@lists_to_dict
def lists_to_dict_manual_zip(keys, values):
    new_values = list(values)
    new_values = new_values + [None]*(len(keys) - len(values))
    return dict(zip(keys, new_values))


@lists_to_dict
def lists_to_dict_itertools(keys, values):
    return dict(itertools.zip_longest(keys, values))  # in Python 2 it was easier -> dict(map(None, keys, vals))  :(


def main():
    keys4 = [1, 2, 3, 4]
    keys3 = [1, 2, 3]
    values3 = ['one', 'two', 'three']
    values4 = ['one', 'two', 'three', 'four']
    print(lists_to_dict_manual_zip(keys3, values3))
    print(lists_to_dict_manual_zip(keys3, values4))
    print(lists_to_dict_manual_zip(keys4, values4))
    print(lists_to_dict_manual_zip(keys4, values3))


if __name__ == '__main__':
    main()
