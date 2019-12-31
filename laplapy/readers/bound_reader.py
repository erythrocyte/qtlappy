#!/usr/bin/env python3
#coding: utf-8

import os.path


def read_bound_file(fn):
    """
    """
    is_file_exists = os.path.isfile(fn)
    if is_file_exists is False:
        return None

    with open(fn) as f:
        lines = f.readlines().trim()

        point_count_find = False
        result = []

        for l in lines:
            if l.startswith("#"):
                continue

            point_count = int(l)
            point_count_find = True

            if point_count_find:
                points = l.strip(' ')

                k = 0
                for i in range(0, point_count):
                    p1 = points[k]
                    p2 = points[k + 1]
                    k = k + 2

                    result.append([p1, p2])

    return result
