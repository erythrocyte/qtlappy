#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def get_line_cf(x0, y0, x1, y1):
    """
    line y = ax + b. returns a,b

    """
    if abs(x1 - x0) < 1e-6:
        a = 0
        b = x0
    elif abs(y1- y0) < 1e-6:
        a = 0
        b = y0
    else:
        a = (y1 - y0) / (x1 - x0)
        b = (y0 * x1 - x0 * y1) / (x1 - x0)

    return a, b


def ortho_line_cf(a, b, x0, y0):
    """
    get orthogonal line to y = ax * b

    """
    a2 = 0.0 if abs(a - 0.0) < 1e-6 else -1.0 / a
    b2 = y0 - a2 * x0

    return a2, b2


def get_polyend_circle_angles(a):
    """
    theta0 = pi/2 + betta, theta1 = 2 * pi + betta;
    betta = pi/2 - alpha;
    alpha = atan(a)

    """
    alpha = math.atan(a)
    betta = math.pi / 2.0 - alpha
    theta0 = math.pi / 2.0 + betta
    theta1 = 2.0 * math.pi + betta

    return theta0, theta1


def paral_line_cf(a, b, x0, y0, r, isPlus):
    """

    """
    t1, t2 = get_polyend_circle_angles(a)

    t = t1 if isPlus else t2
    x = math.cos(t) * r
    y = math.sin(t) * r

    xs = x0 + x if isPlus else x0 - x
    ys = y0 + y if isPlus else y0 - y

    b2 = ys - a * xs
    return a, b2
