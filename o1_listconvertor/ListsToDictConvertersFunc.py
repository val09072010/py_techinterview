#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import itertools


def lists_to_dict_manual_zip(keys, values):
    """
    Есть два списка разной длины. В первом содержатся ключи, а во втором — значения.
    Напишите функцию, которая создает из этих ключей и значений словарь.
    Если какому-то ключу не хватило значения, в словаре должно быть значение None.
    Implemented via zip function
    """
    new_values = values[:]
    if len(keys) > len(values):
        new_values = new_values + [None]*(len(keys) - len(values))
    res = dict(zip(keys, new_values))
    return res


def lists_to_dict_itertools(keys, values):
    """
    Есть два списка разной длины. В первом содержатся ключи, а во втором — значения.
    Напишите функцию, которая создает из этих ключей и значений словарь.
    Если какому-то ключу не хватило значения, в словаре должно быть значение None.
    Implemented via itertools.zip_longest
    """

    if len(keys) <= len(values):
        res = dict(zip(keys, values))
    else:
        res = dict(itertools.zip_longest(keys, values))  # in Python 2 it was easier -> dict(map(None, keys, vals))  :(
    return res
