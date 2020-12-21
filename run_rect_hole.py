#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from src.lappy.models.field import Field
from src.lappy.services.mesh_maker_2d import MeshMaker2D
from src.lappy.models.settings.global_setts import GlobalSetts
import matplotlib.pyplot as plt
import triangle as tr


def main():
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


def a():
    import numpy as np
    import matplotlib
    from matplotlib.patches import Polygon
    from matplotlib.collections import PatchCollection
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    N = 3
    # x = np.random.rand(N)
    # y = np.random.rand(N)
    # radii = 0.1*np.random.rand(N)
    patches = []
    # for x1, y1, r in zip(x, y, radii):
    #     circle = Circle((x1, y1), r)
    #     patches.append(circle)

    # x = np.random.rand(N)
    # y = np.random.rand(N)
    # radii = 0.1*np.random.rand(N)
    # theta1 = 360.0*np.random.rand(N)
    # theta2 = 360.0*np.random.rand(N)
    # for x1, y1, r, t1, t2 in zip(x, y, radii, theta1, theta2):
    #     wedge = Wedge((x1, y1), r, t1, t2)
    #     patches.append(wedge)

    # Some limiting conditions on Wedge
    # patches += [
    #     Wedge((.3, .7), .1, 0, 360),             # Full circle
    #     Wedge((.7, .8), .2, 0, 360, width=0.05),  # Full ring
    #     Wedge((.8, .3), .2, 0, 45),              # Full sector
    #     Wedge((.8, .3), .2, 45, 90, width=0.10),  # Ring sector
    # ]

    xy = np.empty((0, 2))
    xy = np.append(xy, np.array([[-1, 1]]), axis=0)
    xy = np.append(xy, np.array([[2, 3]]), axis=0)
    xy = np.append(xy, np.array([[0, 0]]), axis=0)
    xy2 = np.array([(1, 1), (2, 3), (0, 0)])
    # xy = np.append(xy, [2, 3])
    # xy = np.append(xy, [0, 0])
    # for i in range(10):
    #     np.append(xy, (i, i * i - i))

    # xy = np.array([(1, 1)])
    pol = Polygon(xy, True)
    patches.append(pol)

    
    pol = Polygon(xy2, True)
    patches.append(pol)

    # for i in range(N):
    #     xy = np.random.rand(N, 2)
    #     polygon = Polygon(xy, True)
    #     patches.append(polygon)

    colors = 12*np.random.rand(len(patches))
    p = PatchCollection(patches, alpha=0.4)
    p.set_array(np.array(colors))
    ax.add_collection(p)
    fig.colorbar(p, ax=ax)

    ax.autoscale()

    plt.show()


def b():
    from src.lappy.services.vtk_saver import save_vtk

    pts = ([1, 1], [2, 3], [0, 0])
    seg = ([0, 1], [1, 2], [2, 0])

    save_vtk('1.vtk', 'test polygon', 'index', pts, seg)
    print('test vtk save done')


if __name__ == '__main__':
    # main()
    b()
