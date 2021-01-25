#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

from src.lappy.services import geom_oper


def line(self, p1, p2, n):
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
