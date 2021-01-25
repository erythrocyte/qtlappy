#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from src.lappy.models.point import Point


class Vector(object):
    def __init__(self, p_begin: Point, p_end: Point):
        """
        """
        self.p_begin = p_begin
        self.p_end = p_end

    def components(self):
        x = self.p_end.x - self.p_begin.x
        y = self.p_end.y - self.p_begin.y
        return [x, y]

    def lenght(self):
        x, y = self.components()
        return math.sqrt(x**2 + y**2)
