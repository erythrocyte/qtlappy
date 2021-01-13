#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from src.lappy.models.point import Point


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


def get_intersect_point(a1, b1, a2, b2):
    """
    The point of intersection of two lines.
    If lines parallel then None is returned

    """
    if a1 is None and a2 is None:
        return None, None

    if a1 is None and abs(a2 - 0.0) < 1e-6:
        return b1, b2

    if a2 is None and abs(a1 - 0.0) < 1e-6:
        return b2, b1

    if abs(a2 - a1) < 1e-6:
        return None, None

    x = (b2 - b1) / (a1 - a2)
    y = (a1 * b2 - b1 * a2) / (a1 - a2)

    return x, y


# Given three colinear points p, q, r, the function checks if
# point q lies on line segment 'pr'
def __on_segment(p: Point, q: Point, r: Point):
    if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
            (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False


def __orientation(p: Point, q: Point, r: Point):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Colinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise

    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
    # for details of below formula.

    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):  # Clockwise orientation
        return 1
    elif (val < 0):  # Counterclockwise orientation
        return 2
    else:  # Colinear orientation
        return 0


def is_segments_intersect(p1: Point, q1: Point, p2: Point, q2: Point):
    """
    The main function that returns true if
    the line segment 'p1q1' and 'p2q2' intersect.
    """

    # Find the 4 orientations required for
    # the general and special cases
    o1 = __orientation(p1, q1, p2)
    o2 = __orientation(p1, q1, q2)
    o3 = __orientation(p2, q2, p1)
    o4 = __orientation(p2, q2, q1)

    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True

    # Special Cases

    # p1 , q1 and p2 are colinear and p2 lies on segment p1q1
    if ((o1 == 0) and __on_segment(p1, p2, q1)):
        return True

    # p1 , q1 and q2 are colinear and q2 lies on segment p1q1
    if ((o2 == 0) and __on_segment(p1, q2, q1)):
        return True

    # p2 , q2 and p1 are colinear and p1 lies on segment p2q2
    if ((o3 == 0) and __on_segment(p2, p1, q2)):
        return True

    # p2 , q2 and q1 are colinear and q1 lies on segment p2q2
    if ((o4 == 0) and __on_segment(p2, q1, q2)):
        return True

    # If none of the cases
    return False
