#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import triangle as tr
# from src.lappy.models.field import Field


class MeshMaker2D:
    """
    class definition

    """

    def triangulate(self, field, setts):
        """
        definition

        """
        # geom = self.__make_geom(field.bound, field.wells, setts)
        geom = self.__make_geom(field.bound, None, setts)
        mesh = tr.triangulate(geom, 'qpa0.1')

        return mesh

    def __make_geom(self, bound, wells, setts):
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
                wx = well.track[0].x
                wy = well.track[0].y
                hls.append([wx, wy])
                if well.is_vert:
                    pts_well, seg_well = self.__circle(
                        wx,
                        wy,
                        setts.well.n_vert,
                        well.radius)

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

    def __polygon(self, bound):
        """
        make outer bound as polygon from

        """

        point_count = len(bound.points)
        seg = []

        for i in range(point_count-1):
            seg.append([i, i + 1])

        seg.append([point_count - 1, 0])
        return bound.points, seg
