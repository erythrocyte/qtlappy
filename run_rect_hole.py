#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from src.lappy.models import bound
# from src.lappy.models import bound
# from laplapy.readers import bound_reader, holes_reader
# from laplapy.classes import gridTri2d
# # import numpy as np
# import matplotlib.pyplot as plt
# import triangle as tr


def main():
    # read boundary points
    dirname = os.path.realpath('')
    fn_bound_points = 'examples/data/rect_hole/boundary.json'
    fn_bound_points = os.path.join(dirname, fn_bound_points)
    bnd = bound.Bound.from_json(fn_bound_points)
    # bound_points = bound_reader.read_bound_file_json(fn_bound_points)

    # read holes
    # fn_holes = 'examples/data/rect_hole/holes.txt'
    # fn_holes = os.path.join(dirname, fn_holes)
    # wells = holes_reader.read_holes_file(fn_holes)

    # gridMaker = gridTri2d.GridTri2D()
    # A = gridMaker.make_tri_grid(bound_points, wells)
    # B = tr.triangulate(A, 'qpa0.1')
    # ax = plt.axes()
    # # tr.compare(plt, A, B)
    # tr.plot(ax, **B)
    # ax.get_xaxis().set_visible(True)
    # ax.get_yaxis().set_visible(True)
    # plt.show()


if __name__ == '__main__':
    main()
