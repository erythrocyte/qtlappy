#!/usr/bin/env python3
# coding: utf-8

from src.lappy.models.well import Well
from src.lappy.models.point import Point
from src.lappy.models.vector import Vector
from src.lappy.services import geom_oper, vect_oper
import math
import numpy as np


class HorWellMaker(object):
    """
    """

    def make(self, well: Well, nw: int, hnw: int):
        """
        """
        temp_points = self.__get_line_points(well)
        print("a")
        # [pts, seg] = self.__half_circle(pbs1, track[0], nw, rw, not cw)

        # # seg_count = len(seg)
        # # [ptsw, segw] = self.__line(pbs2, track[1], hnw)
        # # pts = np.vstack([pts, ptsw])
        # # seg = np.vstack([seg, segw + seg_count])
        # # seg_count = seg_count + segw.shape[0]

        # return [pts, seg]
        return temp_points

    def __get_line_points(self, well: Well):
        """
        """
        rw = well.radius
        track = well.track
        result = []

        for i in range(len(well.track)-1):
            p0, p1 = track[i], track[i + 1]
            pl, pr = self.__get_bound_points(p0, p1, rw)
            result.append([pl, pr])
            pl, pr = self.__get_bound_points(p1, p0, rw)
            result.append([pl, pr])

        # swap left and right
        self.__order_left_right_points(result)

        return result

    def __order_left_right_points(self, points):
        """
        Args:
            points : list[[Points, Point]]            
        """

        for i in range(len(points)-1):
            p1, p2 = points[i]
            q1, q2 = points[i + 1]
            if geom_oper.is_segments_intersect(p1, q1, p2, q2):
                points[i+1][0], points[i+1][1] = points[i+1][1], points[i+1][0]
            elif geom_oper.is_segments_intersect(p1, q1, p2, q2):
                points[i+1][0], points[i+1][1] = points[i+1][1], points[i+1][0]

    def __get_bound_points(self, pt_main, pt2, rw):
        """
        """
        [x0, y0] = [pt_main.x, pt_main.y]
        [x1, y1] = [pt2.x, pt2.y]
        [asg, bsg] = geom_oper.get_line_cf(x0, y0, x1, y1)
        [ap, bp] = geom_oper.ortho_line_cf(asg, bsg, x0, y0)

        x2 = x0 + 1.0
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
        pts = np.stack([R * np.cos(theta) + p0.x, R *
                        np.sin(theta) + p0.y], axis=1)
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
