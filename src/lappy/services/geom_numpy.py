#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

from src.lappy.models.point import Point
from src.lappy.services import geom_oper


def line(p1: Point, p2: Point, n: int,
         use_first_pt=True,
         use_last_pt=True):
    """
    returns line points and segments
    between given points with step 'n'

    returns `[None, None]` if:
        a. 'n <= 0';
        b. 'p1' or 'p2' is None

    return [pts, seg]:
        pts - numpy array of points
        seg - numpy array of segments

    args:
        p1[] - Point begin
        p2 - Point end
        n - line division step
        use_first_pt - include 'p1' to result
        use_last_pt - include 'p2' to result
    """

    if n is None or use_first_pt is None or use_last_pt is None:
        return None, None

    if n == 1 and (not use_last_pt or not use_first_pt):
        return None, None

    if n == 2 and not use_first_pt and not use_last_pt:
        return None, None

    if n <= 0 or p1 is None or p2 is None:
        return None, None

    [x0, y0] = [p1.x, p1.y]
    [x1, y1] = [p2.x, p2.y]
    [a, b] = geom_oper.get_line_cf(x0, y0, x1, y1)

    if a is None or b is None:
        return None, None

    pts = np.empty((0, 2))
    seg = np.empty((0, 2), int)

    n0 = 0 if use_first_pt else 1
    n1 = n+1 if use_last_pt else n

    dx = (x1 - x0) / float(n)

    index = 0
    for i in range(n0, n1):
        x = x0 + dx * i
        y = a * x + b
        pts = np.append(pts, np.array([[x, y]]), axis=0)
        if index > 0:
            seg = np.append(seg, np.array([[index-1, index]]), axis=0)
        index += 1

    return [pts, seg]


def sector(p0: Point, pc: Point, n: int, clockwise: bool, angle: float,
           use_first_pt=True, use_last_pt=True):
    """

    returns points and segments

    returns[pts, seg]:
        pts - numpy array of points
        seg - numpy array of segments

    args:
        p0 - start point
        pc - center point (imagine circle)
        n - step count
        clokwise - rotate direction
    """
    # check for suits

    if n is None or use_last_pt is None or use_first_pt is None:
        return None, None

    if angle is None:
        return None, None

    if n == 1 and (not use_last_pt or not use_first_pt):
        return None, None

    if n == 2 and not use_first_pt and not use_last_pt:
        return None, None

    if n <= 0 or p0 is None or pc is None:
        return None, None

    n0 = 0 if use_first_pt else 1
    n1 = n+1 if use_last_pt else n
    pts = np.empty((0, 2))
    seg = np.empty((0, 2))

    n0 = 0 if use_first_pt else 1
    n1 = n+1 if use_last_pt else n

    dtet = angle / float(n) * (1 if clockwise else -1)

    for i in range(n0, n1):
        tet = dtet * i
        p = geom_oper.rotate_point(p0, pc, tet)
        pts = np.append(pts, np.array([p]), axis=0)
        if i > 0:
            seg = np.append(seg, np.array([[i-1, i]]), axis=0)
    return pts, seg
