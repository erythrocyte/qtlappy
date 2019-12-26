#!/usr/bin/env python3
#coding: utf-8

import matplotlib.pyplot as plt
from src import lapltri
import triangle as tr

# from matplotlib.patches import Polygon


def main():
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
    # polygon = Polygon([[0, 0], [0, 0]], facecolor='y')  # dummy data for xs,ys
    # update_polygon(-1)
    # plt.gca().add_patch(polygon)
    # plt.gcf().canvas.mpl_connect('motion_notify_event', motion_notify)
    plt.show()


if __name__ == '__main__':
    main()
