#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from typing import List

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

    pts = np.empty((0, 2))
    seg = np.empty((0, 2), int)

    if n is None or use_first_pt is None or use_last_pt is None:
        return None, None

    if n == 1:
        if use_first_pt:
            pts = np.append(pts, np.array([[p1.x, p1.y]]), axis=0)
        if use_last_pt:
            pts = np.append(pts, np.array([[p2.x, p2.y]]), axis=0)
        if use_last_pt and use_first_pt:
            seg = np.append(seg, np.array([[0, 1]]), axis=0)
        return pts, seg

    if n == 2 and not use_first_pt and not use_last_pt:
        return None, None

    if n <= 0 or p1 is None or p2 is None:
        return None, None

    [x0, y0] = [p1.x, p1.y]
    [x1, y1] = [p2.x, p2.y]
    [a, b] = geom_oper.get_line_cf(x0, y0, x1, y1)

    if a is None and b is None:
        return None, None

    n0 = 0 if use_first_pt else 1
    n1 = n+1 if use_last_pt else n

    if a is None:  # x = const
        pts = __x_const_line(y0, y1, x0, n, n0, n1)
    elif abs(a - 0.0) < 1e-8:
        pts = __y_const_line(x0, x1, y0, n, n0, n1)
    else:
        pts = __xy_line(x0, x1, n, n0, n1, a, b)

    N = len(pts)
    i = np.arange(N-1)
    seg = np.stack([i, i + 1], axis=1)  # % N

    return [pts, seg]


def sector(p0: Point, pc: Point, n: int, p_track: Point, angle: float,
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
        p_track - well track sector another point (sector = [pc, p_track])
    """
    # check for suits

    pts = np.empty((0, 2))
    seg = np.empty((0, 2), int)

    if n is None or use_last_pt is None or use_first_pt is None:
        return None, None

    if angle is None:
        return None, None

    if n == 1:
        if not use_first_pt and not use_last_pt:
            return None, None
        if use_first_pt and not use_last_pt:
            pts = np.append(pts, np.array([[p0.x, p0.y]]), axis=0)
            return pts, seg

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

    dtet = angle / float(n)

    n_aver = (n1 + n0) / 2
    tet = dtet * n_aver
    p = geom_oper.rotate_point(p0, pc, tet)
    change_dir = __need_change_dir(p0, pc, p_track, p)
    if change_dir:
        dtet = - dtet

    index = 0
    for i in range(n0, n1):
        tet = dtet * i
        p = geom_oper.rotate_point(p0, pc, tet)
        pts = np.append(pts, np.array([p]), axis=0)
        if index > 0:
            seg = np.append(seg, np.array([[i-1, i]]), axis=0)
        index += 1
    return pts, seg


def __need_change_dir(p1: Point, pc: Point, p_track: Point, pl: List):
    dx = p1.x - pc.x
    dy = p1.y - pc.y

    p2 = Point(pc.x - dx, pc.y - dy, -1)
    pt = Point(pl[0], pl[1], -1)
    return geom_oper.is_point_inside_triangle(pt, p1, p2, p_track)


def __x_const_line(y0, y1, x, n, n0, n1):
    """
    """
    pts = np.empty((0, 2))

    dy = (y1 - y0) / float(n)

    for i in range(n0, n1):
        y = y0 + i * dy
        pts = np.append(pts, np.array([[x, y]]), axis=0)

    return pts


def __y_const_line(x0, x1, y, n, n0, n1):
    """
    """
    pts = np.empty((0, 2))

    dx = (x1 - x0) / float(n)

    for i in range(n0, n1):
        x = x0 + i * dx
        pts = np.append(pts, np.array([[x, y]]), axis=0)

    return pts


def __xy_line(x0, x1, n, n0, n1, a, b):
    """
    """

    pts = np.empty((0, 2))
    dx = (x1 - x0) / float(n)

    for i in range(n0, n1):
        x = x0 + dx * i
        y = a * x + b
        pts = np.append(pts, np.array([[x, y]]), axis=0)

    return pts
