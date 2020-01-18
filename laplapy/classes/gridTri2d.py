#!/usr/bin/env python3
#coding: utf-8

import numpy as np
from matplotlib.tri import Triangulation


class GridTri2D:
    def __init__(self):
        self.gridCreated = False

    def make_tri_grid(self, bound, wells):
        """
        definition

        """
        if bound is None:
            return None

        pts_bound, seg_bound = self.__polygon(bound)

        pts = np.vstack([pts_bound])
        seg = np.vstack([seg_bound])

        if wells is None:
            A = dict(vertices=pts, segments=seg)
        else:
            seg_count = len(seg_bound)
            hls = []
            for well in wells:
                wx = well.track[0][0]
                wy = well.track[0][1]
                hls.append([wx, wy])
                if well.isVert:
                    pts_well, seg_well = self.__circle(
                        wx,
                        wy,
                        well.seg_count,
                        well.rw)

                    pts = np.vstack([pts, pts_well])
                    seg = np.vstack([seg, seg_well + seg_count])
                    seg_count = seg_count + seg_well.shape[0]

            A = dict(vertices=pts, segments=seg, holes=hls)

        return A

    def __circle(self, x, y, N, R):
        i = np.arange(N)
        theta = i * 2 * np.pi / N
        pts = np.stack([R * np.cos(theta) + x, R * np.sin(theta) + y], axis=1)
        seg = np.stack([i, i + 1], axis=1) % N
        return pts, seg

    def __rectangle(self, x0, y0, lx, ly):
        pts = [[x0, y0], [lx + x0, y0], [lx + x0, ly + y0], [x0, ly + y0]]
        seg = [[0, 1], [1, 2], [2, 3], [3, 0]]
        return pts, seg

    def __polyhole(self, track, rw

    def __polygon(self, bound_points):
        """
        make outer bound as polygon from

        """

        point_count = len(bound_points)
        seg = []

        for i in range(point_count-1):
            seg.append([i, i + 1])

        seg.append([point_count - 1, 0])
        return bound_points, seg

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