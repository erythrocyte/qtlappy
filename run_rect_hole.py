#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from laplapy.readers import bound_reader  # ,  holes_reader
from laplapy.classes import gridTri2d
import numpy as np
import matplotlib.pyplot as plt
import triangle as tr


def main():
    # read boundary points
    dirname = os.path.realpath('')
    fn_bound_points = 'examples/data/rect_hole/boundary.txt'
    fn_bound_points = os.path.join(dirname, fn_bound_points)
    bound_points = bound_reader.read_bound_file(fn_bound_points)

    # read holes
    # fn_holes = 'examples/data/rect_hole/holes.txt'
    # fn_holes = os.path.join(dirname, fn_holes)
    # holes_points = holes_reader.read_holes_file(fn_holes)

    gridMaker = gridTri2d.GridTri2D()
    pts_bound, seg_bound = gridMaker._GridTri2D__polygon(bound_points)

    pts = np.vstack([pts_bound])
    seg = np.vstack([seg_bound])
    A = dict(vertices=pts, segments=seg)  # , holes=[[]])
    B = tr.triangulate(A)
    ax = plt.axes()
    tr.plot(ax, **B)
    ax.get_xaxis().set_visible(True)
    ax.get_yaxis().set_visible(True)
    plt.show()


if __name__ == '__main__':
    main()
