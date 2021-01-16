#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from src.lappy.models.vector import Vector
from src.lappy.models.point import Point


def get_dot_mult(v1: Vector, v2: Vector):
    x1, y1 = v1.vect_comp()
    x2, y2 = v2.vect_comp()

    return x1 * x2 + y1 * y2


def get_determinant(v1: Vector, v2: Vector):
    x1, y1 = v1.vect_comp()
    x2, y2 = v2.vect_comp()

    return x1 * y2 - y1 * x2


def get_angle(v1: Vector, v2: Vector):
    dot = get_dot_mult(v1, v2)
    det = get_determinant(v1, v2)

    return - math.atan2(det, dot)


def normalize(*args):
    """

    normalize the vector

    args:
        variant 1 : vector to be normalized
        variant 2 : vx: x component of vector to be normalized
                    vy: y component of vector to be normalized
        variant 3:  p_begin : start point of vector to be normalized
                    p_end   : end point of vector to be normalized

    returns:
        list[ux, uy] - vector normalized components
    """

    if len(args) == 1:
        if isinstance(args[0], Vector):
            v = args[0]
            ll = v.lenght()
            x, y = v.components()
            return [x / ll, y / ll]  # todo: divide by zero
    elif len(args) == 2:
        if isinstance(args[0], float):
            vx, vy = args
            ll = math.sqrt(vx**2 + vy**2)
            return [vx / ll, vy / ll]  # todo: zero division
        elif isinstance(args[0], Point):
            p_begin, p_end = args
            vx, vy = (p_end.x - p_begin.x, p_end.y - p_begin.y)
            ll = math.sqrt(vx**2 + vy**2)
            return [vx / ll, vy / ll]  # todo: zero division
