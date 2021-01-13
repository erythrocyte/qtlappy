#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from src.lappy.models.vector import Vector


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
