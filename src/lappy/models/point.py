#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Point(object):
    def __init__(self, x: float, y: float, tp: int):
        self.x = x
        self.y = y
        self.type = tp

    @classmethod
    def from_json(cls, data):
        return cls(x=data['x'], y=data['y'], tp=data['type'])