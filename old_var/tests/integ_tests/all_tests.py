#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import math
from src.lappy.models.field import Field
from src.lappy.services.mesh_maker_2d import MeshMaker2D
from src.lappy.services.hor_well_maker import HorWellMaker
from src.lappy.models.settings.global_setts import GlobalSetts
import matplotlib.pyplot as plt
import triangle as tr


def test_tri():
    dirname = os.path.join(os.path.realpath(''), 'examples/data/rect_hole')
    fn_bound = os.path.join(dirname, 'boundary.json')
    fn_wells = os.path.join(dirname, 'wells.json')

    field = Field.create("test_field", fn_bound, fn_wells)
    print("field created")

    setts = GlobalSetts()
    mesh_maker = MeshMaker2D()
    mesh = mesh_maker.triangulate(field, setts)

    ax = plt.axes()
    tr.plot(ax, **mesh)
    ax.get_xaxis().set_visible(True)
    ax.get_yaxis().set_visible(True)
    plt.show()


def mtp_poly(points):

    if points is None:
        return

    import numpy as np
    import matplotlib
    from matplotlib.patches import Polygon
    from matplotlib.collections import PatchCollection
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    patches = []

    xy = np.empty((0, 2))
    for p in points:
        xy = np.append(xy, np.array([[p.x, p.y]]), axis=0)

    pol = Polygon(xy, True)
    patches.append(pol)

    colors = 12*np.random.rand(len(patches))
    p = PatchCollection(patches, alpha=0.4)
    p.set_array(np.array(colors))
    ax.add_collection(p)
    fig.colorbar(p, ax=ax)

    ax.autoscale()

    plt.show()


def vtk_poly():
    from src.lappy.services.vtk_saver import save_vtk

    pts = ([1, 1], [2, 3], [0, 0])
    seg = ([0, 1], [1, 2], [2, 0])

    save_vtk('1.vtk', 'test polygon', 'index', pts, seg)
    print('test vtk save done')


def test_hw():
    # from src.lappy.services.vtk_saver import save_vtk

    dirname = os.path.join(os.path.realpath(''), 'examples/data/rect_hole')
    fn_bound = os.path.join(dirname, 'boundary.json')
    fn_wells = os.path.join(dirname, 'wells.json')

    field = Field.create("test_field", fn_bound, fn_wells)
    hwm = HorWellMaker()
    # [pts, seg, tp] = hwm.make(field.wells[2], 10, 2)
    [pts, seg, tp] = hwm.make_thin(field.wells[2].track, 10)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    if tp is not None:
        for i, t in enumerate(tp):
            plt.scatter(t.pl.x, t.pl.y, s=10, c='red')
            plt.annotate(f'l{i}', (t.pl.x, t.pl.y))
            plt.scatter(t.pr.x, t.pr.y, s=10, c='blue')
            plt.annotate(f'r{i}', (t.pr.x, t.pr.y))

    # save_vtk('hw.vtk', 'hw', 'index', a, b)

    x_values = []
    y_values = []

    for p in field.wells[2].track:
        x_values.append(p.x)
        y_values.append(p.y)

    plt.plot(x_values, y_values, marker='o')

    x_values.clear()
    y_values.clear()
    for p in pts:
        x_values.append(p[0])
        y_values.append(p[1])
    plt.plot(x_values, y_values, marker='+')
    plt.show()

    print('hw maker test done')


def main():
    # test_hw()
    test_tri()


if __name__ == '__main__':
    main()
