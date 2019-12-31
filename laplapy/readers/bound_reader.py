#!/usr/bin/env python3
#coding: utf-8

import os.path


def read_bound_file(fn):
    """
    """
    is_file_exists = os.path.isfile(fn)
    if is_file_exists is False:
        print("file [{0}] does not exist".format(fn))
        return None

    with open(fn) as f:
        lines = map(str.strip, f.readlines())

        point_count_find = False
        result = []

        for l in lines:
            if l.startswith("#"):
                continue

            if point_count_find is False:
                point_count = int(l)
                point_count_find = True
                continue

            if point_count_find:
                points = l.split(' ')

                k = 0
                for i in range(0, point_count):
                    p1 = points[k]
                    p2 = points[k + 1]
                    k = k + 2

                    result.append([p1, p2])

    return result
