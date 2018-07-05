#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import itertools


def lists_to_dict(inner):
    def decor(inner):
        inner()
    return decor
