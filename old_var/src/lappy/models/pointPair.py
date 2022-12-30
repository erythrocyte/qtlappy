#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.lappy.models.point import Point


class PointPair(object):
    """
    Point class.

    Args:
        x (float):  x coordinate.
        y (float):  y coordinate.
        tp (int):   point type.
    """

    def __init__(self, pl: Point, pr: Point):
        self.pl = pl
        self.pr = pr
