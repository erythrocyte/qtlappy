#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

from src.lappy.models.point import Point
from src.lappy.services import geom_oper


def line(p1: Point, p2: Point, n: int, use_first_pt: bool, use_last_pt: bool):
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
    
    if n <=0 or p1 is None or p2 is None:
        return None, None
    
    [x0, y0] = [p1.x, p1.y]
    [x1, y1] = [p2.x, p2.y]
    [a, b] = geom_oper.get_line_cf(x0, y0, x1, y1)
    pts = np.empty((0, 2))
    seg = np.empty((0, 2), int)

    n0 = 0 if use_first_pt else 1
    n1 = n+1 if use_last_pt else n

    dx = (x1 - x0) / float(n)

    for i in range(n0, n1):
        x = x0 + dx * i
        y = a * x + b
        pts = np.append(pts, np.array([[x, y]]), axis=0)
        if i > 0:
            seg = np.append(seg, np.array([[i-1, i]]), axis=0)

    return [pts, seg]


def sector(p0: Point, pc: Point, n: int, clockwise: bool):
    """

    returns points and segments

    args:
        p0 - start point
        pc - center point (imagine circle)
        n - step count
        clokwise - rotate direction
    """
    i = np.arange(n)
    theta = i * np.pi / n * (-1 if clockwise else 1)
    pts = np.empty((0, 2))
    for t in theta:
        p = geom_oper.rotate_point(p0, pc, t)
        pts = np.append(pts, np.array([p]), axis=0)
    seg = np.stack([i, i + 1], axis=1) % n
    seg = np.delete(seg, -1, axis=0)
    return pts, seg
