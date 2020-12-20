#!/usr/bin/env python3
# coding: utf-8

from src.lappy.models.bound import Bound


class PolygonMaker(object):
    """
    class definition
    """

    def make_polygon(self, bound: Bound):
        """
        make points and segments from bound

        """
        [pts, seg] = self.__polygon(bound)

        return [pts, seg]

    def __polygon(self, bound: Bound):
        """
        make outer bound as polygon from

        """

        point_count = len(bound.points)
        seg = []
        pts = []

        for i in range(point_count-1):
            seg.append([i, i + 1])
        seg.append([point_count - 1, 0])

        for pt in bound.points:
            pts.append([pt.x, pt.y])

        return pts, seg
