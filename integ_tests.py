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


def mtp_poly():
    import numpy as np
    import matplotlib
    from matplotlib.patches import Polygon
    from matplotlib.collections import PatchCollection
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    patches = []

    xy = np.empty((0, 2))
    xy = np.append(xy, np.array([[-1, 1]]), axis=0)
    xy = np.append(xy, np.array([[2, 3]]), axis=0)
    xy = np.append(xy, np.array([[0, 0]]), axis=0)
    xy2 = np.array([(1, 1), (2, 3), (0, 0)])

    pol = Polygon(xy, True)
    patches.append(pol)

    pol = Polygon(xy2, True)
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
    from src.lappy.services.vtk_saver import save_vtk

    dirname = os.path.join(os.path.realpath(''), 'examples/data/rect_hole')
    fn_bound = os.path.join(dirname, 'boundary.json')
    fn_wells = os.path.join(dirname, 'wells.json')

    field = Field.create("test_field", fn_bound, fn_wells)
    hwm = HorWellMaker()
    [a, b] = hwm.make(field.wells[2], 10, 2)

    save_vtk('hw.vtk', 'hw', 'index', a, b)
    print('hw maker test done')


def test_left_right():
    p0 = [0.0, 0.0]
    p1 = [2.0, -1.0]

    pleft = [3.0, -0.5]
    pright = [1.5, -1.5]

    vmain = [p1[0] - p0[0], p1[1] - p0[1]]
    vleft = [pleft[0] - p0[0], pleft[1]-p0[1]]
    vright = [pright[0] - p0[0], pright[1]-p0[1]]

    len_vleft = math.sqrt(vleft[0]**2 + vleft[1]**2)
    len_vright = math.sqrt(vright[0]**2 + vright[1]**2)
    len_vmain = math.sqrt(vmain[0]**2 + vmain[1]**2)

    lm = vmain[0] * vleft[0] + vmain[1] * vleft[1]
    rm = vmain[0] * vright[0] + vmain[1] * vright[1]

    left_alp = math.acos(lm / (len_vmain * len_vleft))
    right_alp = math.acos(rm / (len_vmain * len_vright))

    print(f'left alp = {left_alp}, right alp = {right_alp}')


def main():
    test_left_right()


if __name__ == '__main__':
    main()
