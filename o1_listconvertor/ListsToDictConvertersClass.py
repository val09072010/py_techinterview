#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import itertools


class AbstractListsConverter(object):

    def _equalize(self, keys, values):
        raise NotImplementedError("Please use child classes")

    def lists_to_dict(self, keys, values):
        """
        Есть два списка разной длины.
        В первом содержатся ключи, а во втором — значения.
        Напишите функцию, которая создает из этих ключей и значений словарь.
        Если какому-то ключу не хватило значения, в словаре должно быть None.
        """
        if len(values) >= len(keys):
            res = dict(zip(keys, values))
        else:
            res = self._equalize(keys, values)
        return res


class ManualListsConverter(AbstractListsConverter):
    """
    Implemented via manual padding of values list
    """
    def _equalize(self, keys, values):
        padding = len(keys) > len(values)
        if padding > 0:
            new_values = values[:]
            new_values = new_values + [None] * padding
            return dict(zip(keys, new_values))
        else:
            return dict(zip(keys, values))


class MapListsConverter(AbstractListsConverter):
    """
    Implemented via map(None, ...) feature
    """
    def _equalize(self, keys, values):
        return dict(itertools.zip_longest(keys, values))  # in Python 2 it was easier -> dict(map(None, keys, vals))  :(
