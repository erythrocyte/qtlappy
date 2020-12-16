#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.lappy.models.point import Point


class Well(object):
    def __init__(self, id: int, name: str, is_vert: bool, radius: float, track: list):
        self.id = id
        self.name = name
        self.is_vert = is_vert
        self.radius = radius
        self.track = track

    @ classmethod
    def from_json(cls, data):
        points = list(map(Point.from_json, data["points"]))
        return cls(id=data['id'], name=data['name'], is_vert=data['vert'],
                   radius=data['radius'], track=points)
