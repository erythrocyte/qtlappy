#!/usr/bin/env python3
#coding: utf-8

import os.path
from laplapy.classes import hole


def read_holes_file(fn):
    """
    """
    is_file_exists = os.path.isfile(fn)
    if is_file_exists is False:
        print("file [{0}] does not exist".format(fn))
        return None

    with open(fn) as f:
        lines = map(str.strip, f.readlines())

        holes_count_find = False
        holes = []
        wi = 1

        for l in lines:
            if l.startswith("#"):
                continue

            if holes_count_find is False:
                holes_count = int(l)
                holes_count_find = True
                continue

            if holes_count_find:
                if wi > holes_count:
                    continue

                data = l.split(' ')

                if len(data) != 4:
                    continue

                x = float(data[0])
                y = float(data[1])
                rw = float(data[2])
                pw = float(data[3])

                well = hole.Hole('w{0}'.format(wi), x, y, rw, pw)
                holes.append(well)
                wi = wi + 1

    return holes
