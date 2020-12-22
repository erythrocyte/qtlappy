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
        track = well.track
        cw = False
        [pbs1, pbs2] = self.__get_bound_points(track[0], track[1], rw, cw)
        [pts, seg] = self.__half_circle(pbs1, track[0], nw, rw, not cw)

        # seg_count = len(seg)
        # [ptsw, segw] = self.__line(pbs2, track[1], hnw)
        # pts = np.vstack([pts, ptsw])
        # seg = np.vstack([seg, segw + seg_count])
        # seg_count = seg_count + segw.shape[0]

        return [pts, seg]

    def __get_bound_points(self, pt_main, pt2, rw, clockwise=True):
        [x0, y0] = [pt_main.x, pt_main.y]
        [x1, y1] = [pt2.x, pt2.y]
        [asg, bsg] = geom_oper.get_line_cf(x0, y0, x1, y1)
        [ap, bp] = geom_oper.ortho_line_cf(asg, bsg, x0, y0)

        x2 = x0 + 1.0 if clockwise else -1.0
        y2 = ap * x2 + bp

        vx = x2 - x0
        vy = y2 - y0
        lv = math.sqrt(vx**2 + vy**2)
        ux = vx / lv
        uy = vy / lv

        xa = x0 + rw * ux
        ya = y0 + rw * uy
        p0 = Point(xa, ya, -1)

        xb = x0 - rw * ux
        yb = y0 - rw * uy
        p1 = Point(xb, yb, -1)

        return [p0, p1]

    def __half_circle(self, p, p0, N, R, clockwise):
        i = np.arange(N)
        theta0 = math.acos(p.x/R)
        theta = theta0 + i * np.pi / N if clockwise else theta0 - i * np.pi / N
        pts = np.stack([R * np.cos(theta) + p0.x, R * np.sin(theta) + p0.y], axis=1)
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

        for i in range(1, n + 1):
            x = x0 + (x1 - x0) / n * i
            y = a * x + b
            pts = np.append(pts, np.array([[x, y]]), axis=0)
            seg = np.append(seg, np.array([[i-1, i]]), axis=0)

        return [pts, seg]

    def __point_left_right(self, pm, p0, p1):
        """
        args:
            pm (Point) : main point to find "left" and "right" points
            p0 (Point) : point before ${pm} in track
            p1 (Point) : point after ${pm} in track
        """

        
