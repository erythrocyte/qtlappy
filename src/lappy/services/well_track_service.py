# !/usr/bin/env python3
# -*- coding: utf-8 -*-


from src.lappy.models.vector import Vector
from src.lappy.services import vect_oper

import math


def well_track_suits(track):
    """
    returns:    True is well track is suitable for build area
                around else False
    """

    if len(track) == 2:  # simple line
        return True

    for k, t in enumerate(track):
        if k == len(track)-2:
            break
        v1 = make_vector(track, k + 1, k)
        v2 = make_vector(track, k + 1, k + 2)

        ang = abs(vect_oper.get_angle(v1, v2))
        if ang > (89.0 * math.pi / 180.0) / 2.0:
            return False

    return True


def make_vector(track, k_begin, k_end):
    p0 = track[k_begin]
    p1 = track[k_end]
    return Vector(p0, p1)
