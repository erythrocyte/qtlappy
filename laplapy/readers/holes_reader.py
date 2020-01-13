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

        for l in lines:
            if l.startswith("#"):
                continue

            if holes_count_find is False:
                # holes_count = int(l)
                holes_count_find = True
                continue

            if holes_count_find:
                data = l.split(' ')

                well_index = int(data[0])
                rw = float(data[1])
                well_type = int(data[2])
                seg_count = int(data[3])

                track_point_count = int(data[4])

                track = []
                k = 5
                for i in range(track_point_count):
                    x = float(data[k + i])
                    y = float(data[k + i + 1])
                    track.append([x, y])
                    k = k + 1

                well = hole.Hole(well_index, track, rw, well_type == 0, seg_count)
                holes.append(well)

    return holes
