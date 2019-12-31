#!/usr/bin/env python3
#coding: utf-8

import numpy as np
from matplotlib.tri import Triangulation


class GridTri2D:
    def __init__(self):
        self.gridCreated = False

    def make_tri_grid(self):
        a = False
        if a:
            pts0, seg0 = self.__circle(36, 1.0)
        else:
            pts0, seg0 = self.__rectangle(-1, -1, 2, 2)
        pts1, seg1 = self.__circle(36, 0.5)
        seg_count = seg0.shape[0] if a else len(seg0)
        pts = np.vstack([pts0, pts1])
        seg = np.vstack([seg0, seg1 + seg_count])

        A = dict(vertices=pts, segments=seg, holes=[[0, 0.1]])
        return A

    def __circle(self, N, R):
        i = np.arange(N)
        theta = i * 2 * np.pi / N
        pts = np.stack([np.cos(theta), np.sin(theta)], axis=1) * R
        seg = np.stack([i, i + 1], axis=1) % N
        return pts, seg

    def __rectangle(self, x0, y0, lx, ly):
        pts = [[x0, y0], [lx + x0, y0], [lx + x0, ly + y0], [x0, ly + y0]]
        seg = [[0, 1], [1, 2], [2, 3], [3, 0]]
        return pts, seg

    def make_tri_grid_matplot(self):
        """
        Create a Triangulation.

        """

        n_angles = 16
        n_radii = 5
        min_radius = 0.25
        radii = np.linspace(min_radius, 0.95, n_radii)
        angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
        angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
        angles[:, 1::2] += np.pi / n_angles
        x = (radii*np.cos(angles)).flatten()
        y = (radii*np.sin(angles)).flatten()
        triang = Triangulation(x, y)
        triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                                 y[triang.triangles].mean(axis=1)) < min_radius)

        return triang
