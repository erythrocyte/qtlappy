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
    if a is None:  # x=const
        a2 = 0
        b2 = y0
    elif abs(a - 0.0) < 1e-6:  # y=const
        a2 = None
        b2 = x0
    else:
        a2 = -1.0 / a
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


def is_segments_intersect(p1: Point, q1: Point, p2: Point, q2: Point,
                          continuous=False):

    # Before anything else check if lines have a mutual abcisses
    interval_1 = [min(p1.x, q1.x), max(p1.x, q1.x)]
    interval_2 = [min(p2.x, q2.x), max(p2.x, q2.x)]

    if interval_1[1] < interval_2[0]:
        print('No mutual abcisses!')
        return False, None

    if point_on_segment(p1, p2, q2):
        return True, p1
    if point_on_segment(q1, p2, q2):
        return True, q1

    # Try to compute interception
    def line(p1, p2):
        A = (p1.y - p2.y)
        B = (p2.x - p1.x)
        C = (p1.x*p2.y - p2.x*p1.y)
        return A, B, -C

    L1 = line(p1, q1)
    L2 = line(p2, q2)

    D = L1[0]*L2[1] - L1[1]*L2[0]
    Dx = L1[2]*L2[1] - L1[1]*L2[2]
    Dy = L1[0]*L2[2] - L1[2]*L2[0]

    if D != 0:
        x = Dx / D
        y = Dy / D
        p = Point(x, y, -1)
        if continuous:  # continuous parameter allows switching between line
            # and line segment interception
            return True, p
        else:
            d11 = get_dist(p, p1)
            d12 = get_dist(p, q1)
            d1 = get_dist(p1, q1)
            d21 = get_dist(p, p2)
            d22 = get_dist(p, q2)
            d2 = get_dist(p2, q2)
            if abs(d1 - (d11 + d12)) > 1e-6 or abs(d2 - (d21 + d22)) > 1e-6:
                print('Intersection out of bound at [%.2f, %.2f]' % (p.x, p.y))
                return False, None
            else:
                return True, p
    else:
        if (Dx == 0 or Dy == 0):
            print('segments parallel')
        return False, None


def point_on_line(p, pl1, pl2):
    """
    """

    a, b = get_line_cf(pl1.x, pl1.y, pl2.x, pl2.y)
    if a is None:
        return True if abs(p.y - pl1.x) < 1e-6 else False

    py = a * p.x + b
    return True if abs(py - p.y) < 1e-6 else False


def point_on_segment(p, pl1, pl2):
    """
    """
    res = point_on_line(p, pl1, pl2)
    if not res:
        return False

    d1 = get_dist(p, pl1)
    d2 = get_dist(p, pl2)
    d = get_dist(pl1, pl2)

    return True if abs(d - (d1 + d2)) < 1e-6 else False


def get_dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def rotate_point(p: Point, pc: Point, angle: float):
    """

    calculates the point `p0` by circle around the point `pc`
    for the given angle

    args:
        p - start point to rotate
        pc - circle center
        angle - angle in radians
    """
    # if angle < 0. or p.x < pc.x or p.y < pc.y:
    #     angle = 2. * math.pi - angle
        
    if p.x < pc.x or p.y < pc.y:
        angle = 2. * math.pi - angle

    s = math.sin(angle)
    c = math.cos(angle)

    result = Point(p.x, p.y, -1)

    # translate point back to origin:
    result.x -= pc.x
    result.y -= pc.y

    # rotate point
    xnew = result.x * c - result.y * s
    ynew = result.x * s + result.y * c

    # translate point back:
    result.x = xnew + pc.x
    result.y = ynew + pc.y
    return [result.x, result.y]


def is_point_inside_triangle(pt: Point, a: Point, b: Point, c: Point):
    """
    define is given point 'pt' inside the triangle

    args:
        a,b,c - triangle nodes
        pt - point
    """
    
    a1 = (a.x - pt.x) * (b.y - a.y) - (b.x - a.x) * (a.y - pt.y)
    a2 = (b.x - pt.x) * (c.y - b.y) - (c.x - b.x) * (b.y - pt.y)
    a3 = (c.x - pt.x) * (a.y - c.y) - (a.x - c.x) * (c.y - pt.y)

    if a1 <= 0 and a2 <= 0 and a3 <= 0:
        return True

    if a1 >= 0 and a2 >= 0 and a3 >= 0:
        return True

    return False
