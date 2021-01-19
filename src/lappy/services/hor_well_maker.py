#!/usr/bin/env python3
# coding: utf-8

from src.lappy.models.well import Well
from src.lappy.models.point import Point
from src.lappy.models.pointPair import PointPair
from src.lappy.models.vector import Vector
from src.lappy.services import geom_oper, vect_oper
from src.lappy.services import well_track_service
import math
import numpy as np


class HorWellMaker(object):
    """
    """

    class PointPairs(object):
        def __init__(self):
            self.pairs = []

    def make(self, well: Well, nw: int, hnw: int):
        """
        """

        # check well track suitable
        if not well_track_service.well_track_suits(well.track):
            print('well track is not suitable: sharp angles')
            return None, None, None

        tp = self.__get_line_points(well)
        rw = well.radius
        [pts, seg] = self.__sector(tp[0].pl,
                                   well.track[0],
                                   nw, rw, False)

        ltp = len(tp)
        seg_count = len(seg)
        for i in range(ltp-1):
            [ptsw, segw] = self.__line(tp[i].pr, tp[i+1].pr, hnw)
            pts = np.vstack([pts, ptsw])
            seg = np.vstack([seg, segw + seg_count])
            seg_count = seg_count + segw.shape[0]

        [pts1, seg1] = self.__sector(tp[ltp-1].pr,
                                     well.track[ltp-2],
                                     nw, rw, False)
        pts = np.vstack([pts, pts1])
        seg = np.vstack([seg, seg1 + seg_count])
        seg_count = seg_count + seg1.shape[0]

        for i in range(ltp-1):
            [ptsw, segw] = self.__line(
                tp[ltp-1 - i].pl, tp[ltp-1 - (i+1)].pl, hnw)
            pts = np.vstack([pts, ptsw])
            seg = np.vstack([seg, segw + seg_count])
            seg_count = seg_count + segw.shape[0]

        return pts, seg, tp

    def __get_line_points(self, well: Well):
        """
        """
        rw = well.radius
        track = well.track
        prs = [self.PointPairs() for i in range(len(well.track))]

        for i in range(len(well.track)-1):
            p0, p1 = track[i], track[i + 1]
            pr1 = self.__get_bound_points(p0, p1, rw)
            pr2 = self.__get_bound_points(p1, p0, rw)
            prs[i].pairs.append(pr1)
            prs[i+1].pairs.append(pr2)

        # swap left and right
        self.__order_left_right_points(prs, well.track)
        result = self.__merge_points(prs, well.track, well.radius)

        return result

    def __order_left_right_points(self, pts, track):
        """
        Args:
            pts : list[PointPairs]
            track : well track
        """

        def check_swap(p1, q1, p2, q2):
            res, p = geom_oper.is_segments_intersect(p1, q1, p2, q2)
            return True if res else False

        def do_swap(pts, k, j):
            pts[k].pairs[j].pl, pts[k].pairs[j].pr = \
                pts[k].pairs[j].pr, pts[k].pairs[j].pl

        def intersect_track(p1, q1, track):
            for k in range(len(track)-1):
                p2 = track[k]
                q2 = track[k+1]
                res = check_swap(p1, q1, p2, q2)
                if res:
                    return True

            return False

        for k, p in enumerate(pts):
            for j in range(1, len(p.pairs)+1):
                if k == len(pts)-1 and j == len(p.pairs):
                    continue

                p1 = p.pairs[j-1].pr
                q1 = pts[k+1].pairs[0].pr if j == len(p.pairs) \
                    else p.pairs[j].pr
                if intersect_track(p1, q1, track):
                    if j == len(p.pairs):
                        a, b = k+1, 0
                    else:
                        a, b = k, j
                    do_swap(pts, a, b)

    def __merge_points(self, prs, track, r):
        result = []

        for i, pr in enumerate(prs):
            while (len(pr.pairs) != 1):
                prs[i].pairs = self.__merge_inner_points(pr.pairs, track[i], r)
            result.append(PointPair(pr.pairs[0].pl, pr.pairs[0].pr))

        return result

    def __merge_inner_points(self, prs, tp, r):
        """

        """
        if len(prs) == 1:
            return prs[0]

        result = []

        for i in range(1, len(prs)):
            pl1, pr1 = prs[i-1].pl, prs[i-1].pr
            pl2, pr2 = prs[i].pl, prs[i].pr

            pl = self.__get_merged_inner_pair(pl1, pl2, tp, r)
            pr = self.__get_merged_inner_pair(pr1, pr2, tp, r)
            pp = PointPair(pl, pr)
            result.append(pp)

        return result

    def __get_merged_inner_pair(self, p1, p2, tp, r):
        """

        """

        e = Point((p1.x + p2.x) / 2.0, (p1.y + p2.y) / 2.0, -1)
        ux, uy = vect_oper.normalize(e, tp)

        x, y = tp.x - r * ux, tp.y - r * uy
        return Point(x, y, -1)

    def __get_bound_points(self, pt_main, pt2, rw):
        """

        returns:
            PointPair with "left" and "right" points
        """

        [x0, y0] = [pt_main.x, pt_main.y]
        [x1, y1] = [pt2.x, pt2.y]
        [asg, bsg] = geom_oper.get_line_cf(x0, y0, x1, y1)
        if asg is None:
            xp0 = x0 + rw
            yp0 = y0
            xp1 = x0 - rw
            yp1 = y0
        elif abs(asg - 0.0) < 1e-6 and abs(bsg - 0.0) < 1e-6:
            xp0 = x0
            yp0 = y0 + rw
            xp1 = x0
            yp1 = y0 - rw
        else:
            [ap, bp] = geom_oper.ortho_line_cf(asg, bsg, x0, y0)

            x2 = x0 + 1.0
            y2 = ap * x2 + bp

            vx, vy = x2 - x0, y2 - y0
            ux, uy = vect_oper.normalize(vx, vy)

            xp0 = x0 + rw * ux
            yp0 = y0 + rw * uy
            xp1 = x0 - rw * ux
            yp1 = y0 - rw * uy

        p0 = Point(xp0, yp0, -1)
        p1 = Point(xp1, yp1, -1)
        result = PointPair(p0, p1)
        return result

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
