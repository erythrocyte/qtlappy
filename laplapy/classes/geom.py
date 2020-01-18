#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def get_line_cf(x0, y0, x1, y1):
    """
    line y = ax + b. returns a,b

    """
    sameX = abs(x1 - x0) < 1e-6
    sameY = abs(y1 - y0) < 1e-6

    if sameX and sameY:
        return None, None

    if sameX:
        a = None
        b = x0
    elif sameY:
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
    a2 = 0.0 if a is None else 0.0 if abs(a - 0.0) < 1e-6 else -1.0 / a
    b2 = y0 - a2 * x0

    return a2, b2


def get_polyend_circle_angles(a, b, isLeft):
    """
    theta0 = pi/2 + betta, theta1 = 2 * pi + betta;
    betta = pi/2 - alpha;
    alpha = atan(a)

    """

    if a is None and b is None:
        return None, None

    alpha = math.pi / 2.0 if a is None else math.atan(a)
    betta = math.pi / 2.0 - alpha
    shift = 0.0 if isLeft else math.pi
    theta0 = betta + shift
    theta1 = theta0 + math.pi

    return theta0, theta1


def paral_line_cf(a, b, r, isPlus):
    """

    """
    if a is None or abs(a - 0.0) < 1e-6:
        b1 = r if isPlus else -r
        b1 = b1 + b
        return a, b1

    alpha = math.atan(a)
    c = r * math.sin(alpha)
    shift = c if isPlus else -c
    b2 = b + shift

    return a, b2

    # t1, t2 = get_polyend_circle_angles(a, b, True)

    # t = t1 if isPlus else t2
    # x = math.cos(t) * r
    # y = math.sin(t) * r

    # xs = x0 + x if isPlus else x0 - x
    # ys = y0 + y if isPlus else y0 - y

    # b2 = ys - a * xs
    # return a, b2
