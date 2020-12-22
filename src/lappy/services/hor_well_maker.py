#!/usr/bin/env python3
# coding: utf-8

from src.lappy.models.well import Well
from src.lappy.models.point import Point
from src.lappy.services import geom_oper
import math
import numpy as np


class HorWellMaker(object):
    """
    """

    def make(self, well: Well, nw: int, hnw: int):
        """
        """
        rw = well.radius
        p = self.__get_bound_points(well.track[0], well.track[1], rw)
        [pts, seg] = self.__half_circle(p, nw, well.radius)

        seg_count = len(seg)
        [ptsw, segw] = self.__line(p, well.track[1], hnw)
        pts = np.vstack([pts, ptsw])
        seg = np.vstack([seg, segw + seg_count])
        seg_count = seg_count + segw.shape[0]

        return [pts, seg]

    def __get_bound_points(self, pt_main, pt2, rw, clockwise=True):
        [x0, y0] = [pt_main.x, pt_main.y]
        [x1, y1] = [pt2.x, pt2.y]
        [asg, bsg] = geom_oper.get_line_cf(x0, y0, x1, y1)
        [ap, bp] = geom_oper.ortho_line_cf(asg, bsg, x0, y0)

        x2 = 4.0
        y2 = ap * x2 + bp

        vx = x2 - x0
        vy = y2 - y0
        lv = math.sqrt(vx**2 + vy**2)
        ux = vx / lv
        uy = vy / lv

        xa = x0 + rw * ux
        ya = y0 + rw * uy

        xb = x0 - rw * ux
        yb = y0 - rw * uy

        return Point(xb, yb, -1) if clockwise else Point(xa, ya, -1)

    def __half_circle(self, p, N, R):
        i = np.arange(N)
        theta = i * np.pi / N
        pts = np.stack([R * np.cos(theta) + p.x, R * np.sin(theta) + p.y], axis=1)
        seg = np.stack([i, i + 1], axis=1) % N
        seg = np.delete(seg, -1, axis=0)
        return pts, seg

    def __line(self, p1, p2, n):
        [x0, y0] = [p1.x, p1.y]
        [x1, y1] = [p2.x, p2.y]
        [a, b] = geom_oper.get_line_cf(x0, y0, x1, y1)
        pts = np.empty((0, 2))
        seg = np.empty((0, 2), int)
        # xy = np.append(xy, np.array([[-1, 1]]), axis=0)
        # xy = np.append(xy, np.array([[2, 3]]), axis=0)
        # xy = np.append(xy, np.array([[0, 0]]), axis=0)

        for i in range(n + 1):
            x = x0 + (x1 - x0) / n * i
            y = a * x + b
            pts = np.append(pts, np.array([[x, y]]), axis=0)
            if (i < n):
                seg = np.append(seg, np.array([[i, i + 1]]), axis=0)

        return [pts, seg]
