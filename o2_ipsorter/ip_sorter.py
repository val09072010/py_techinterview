#!/bin/python -tt
# -*- coding: utf-8 -*-
import sys
import re


def ip_collector(file_name):
    ips = {}
    with open(file_name, "r") as log_file:
        for log_line in log_file:
            match = re.match(r'(\d+\.\d+\.\d+\.\d+)*', log_line)
            key = match.group(0)
            if key not in ips.keys():
                ips[key] = 1
            else:
                ips[key] = ips[key] + 1
    return ips


def ip_sorter(ips, top=10):
    res_len = min(top, len(ips.keys()))
    return sorted(ips.items(), key=tuple_sort, reverse=True)[:res_len]


def tuple_sort(item):
    return item[1]


def main():
    args = sys.argv[1:]
    if not args:
        print('usage: ./ip_sorter.py logfile')
        print('So far we will run it with test file - ./access.test.origin')
        log_file_name = "./access.test.origin"
    else:
        log_file_name = args[1]
    ip_map = ip_collector(log_file_name)
    print(ip_sorter(ip_map))


if __name__ == "__main__":
    main()
