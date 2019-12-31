#!/usr/bin/env python3
#coding: utf-8

import sys
from laplapy import lapltri
import matplotlib.pyplot as plt
import triangle as tr


def main(argv):
    if len(argv) == 0:
        print('bad arguments')
        sys.exit(1)
    contour_file = argv[0]
    print(contour_file)
    grid2dTri = lapltri.GridTri2D()
    # draw_grid_mtplt(grid2dTri)
    draw_grid_triangle(grid2dTri)


def draw_grid_triangle(grid2dTri):
    grid = grid2dTri.make_tri_grid()

    B = tr.triangulate(grid, 'qpa0.05')
    tr.compare(plt, grid, B)
    plt.show()


def draw_grid_mtplt(grid2dTri):
    triang = grid2dTri.make_tri_grid_matplot()

    # Setup plot and callbacks.
    plt.subplot(111, aspect='equal')
    plt.triplot(triang, 'bo-')
    plt.show()


if __name__ == '__main__':
    main(sys.argv[1:])
