#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Point(object):
    """
    Point class.

    Args:
        x (float):  x coordinate.
        y (float):  y coordinate.
        tp (int):   point type.
    """
    def __init__(self, x: float, y: float, tp: int):
        self.x = x
        self.y = y
        self.type = tp

    @classmethod
    def from_dict(cls, data):
        """
        Creates class instance from dictionary.

        Args:
            data (dict):    dictionary with point data.
        """
        return cls(x=data['x'], y=data['y'], tp=data['type'])