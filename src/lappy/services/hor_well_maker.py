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
        tp = self.__get_line_points(well)
        rw = well.radius
        [pts, seg] = self.__sector(tp[0][0],
                                   well.track[0],
                                   nw, rw, False)

        ltp = len(tp)
        seg_count = len(seg)
        for i in range(ltp-1):
            [ptsw, segw] = self.__line(tp[i][1], tp[i+1][1], hnw)
            pts = np.vstack([pts, ptsw])
            seg = np.vstack([seg, segw + seg_count])
            seg_count = seg_count + segw.shape[0]

        [pts1, seg1] = self.__sector(tp[ltp-1][1],
                                     well.track[ltp-2],
                                     nw, rw, False)
        pts = np.vstack([pts, pts1])
        seg = np.vstack([seg, seg1 + seg_count])
        seg_count = seg_count + seg1.shape[0]

        for i in range(ltp-1):
            [ptsw, segw] = self.__line(
                tp[ltp-1 - i][0], tp[ltp-1 - (i+1)][0], hnw)
            pts = np.vstack([pts, ptsw])
            seg = np.vstack([seg, segw + seg_count])
            seg_count = seg_count + segw.shape[0]

        return [pts, seg, tp]

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

    def __order_left_right_points(self, pts):
        """
        Args:
            pts : list[[Points, Point]]            
        """

        for i in range(len(pts)-1):
            p1, p2 = pts[i]
            q1, q2 = pts[i + 1]
            res, p = geom_oper.is_segments_intersect(p1, q1, p2, q2)
            if res:
                pts[i+1][0], pts[i+1][1] = pts[i+1][1], pts[i+1][0]
            else:
                res, p = geom_oper.is_segments_intersect(p1, p2, q1, q2)
                if res:
                    pts[i+1][0], pts[i+1][1] = pts[i+1][1], pts[i+1][0]

    def __get_bound_points(self, pt_main, pt2, rw):
        """
        """
        [x0, y0] = [pt_main.x, pt_main.y]
        [x1, y1] = [pt2.x, pt2.y]
        [asg, bsg] = geom_oper.get_line_cf(x0, y0, x1, y1)
        [ap, bp] = geom_oper.ortho_line_cf(asg, bsg, x0, y0)

        x2 = x0 + 1.0
        y2 = ap * x2 + bp

        vx, vy = x2 - x0, y2 - y0
        lv = math.sqrt(vx**2 + vy**2)
        ux, uy = vx / lv, vy / lv

        p0 = Point(x0 + rw * ux, y0 + rw * uy, -1)
        p1 = Point(x0 - rw * ux, y0 - rw * uy, -1)
        return [p0, p1]

    def __sector(self, p0, pc, N, R, clockwise):
        i = np.arange(N)
        theta = i * np.pi / N * (-1 if clockwise else 1)
        pts = np.empty((0, 2))
        for t in theta:
            p = self.__rotate_point(p0, pc, t)
            pts = np.append(pts, np.array([p]), axis=0)
        seg = np.stack([i, i + 1], axis=1) % N
        seg = np.delete(seg, -1, axis=0)
        return pts, seg

    def __line(self, p1, p2, n):
        [x0, y0] = [p1.x, p1.y]
        [x1, y1] = [p2.x, p2.y]
        [a, b] = geom_oper.get_line_cf(x0, y0, x1, y1)
        pts = np.empty((0, 2))
        seg = np.empty((0, 2), int)

        for i in range(1, n + 1):
            x = x0 + (x1 - x0) / n * i
            y = a * x + b
            pts = np.append(pts, np.array([[x, y]]), axis=0)
            seg = np.append(seg, np.array([[i-1, i]]), axis=0)

        return [pts, seg]

    def __rotate_point(self, p: Point, pc: Point, angle: float):
        s = math.sin(angle)
        c = math.cos(angle)

        result = Point(p.x, p.y, -1)

        # translate point back to origin:
        result.x -= pc.x
        result.y -= pc.y

        # rotate point
        xnew = result.x * c - result.y * s
        ynew = result.x * s + result.y * c

        # translate point back:
        result.x = xnew + pc.x
        result.y = ynew + pc.y
        return [result.x, result.y]

    def __get_angle(self, p0, p1, pc, rw):
        x = math.sqrt((p0.x - p1.x)**2 + (p0.y - p1.y)**2)
        return 2.0 * math.asin(x / 2.0 / rw)
