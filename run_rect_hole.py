#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from src.lappy.models.field import Field
# from src.lappy.models import bound
# from laplapy.readers import bound_reader, holes_reader
# from laplapy.classes import gridTri2d
# # import numpy as np
# import matplotlib.pyplot as plt
# import triangle as tr


def main():
    # read boundary points
    dirname = os.path.join(os.path.realpath(''), 'examples/data/rect_hole')
    fn_bound = os.path.join(dirname, 'boundary.json')
    fn_wells = os.path.join(dirname, 'wells.json')

    field = Field.create("test_field", fn_bound, fn_wells)
    print ("field created")
    # bound_points = bound_reader.read_bound_file_json(fn_bound_points)

    # read holes

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
