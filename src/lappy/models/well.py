#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from src.lappy.models.point import Point


class Well(object):
    """
    Well class.

    Args:
        id (int):               identification index;
        name (str):             well name.
        is_vert(bool):          vertical well attribute.
        radius (float):         well radius.
        track (List[Point]):    well trajectory.
    """
    def __init__(self, id: int, name: str, is_vert: bool,
                 radius: float, track: List[Point]):
        self.id = id
        self.name = name
        self.is_vert = is_vert
        self.radius = radius
        self.track = track

    @ classmethod
    def from_dict(cls, data: dict):
        """
        Creates class instance from dictionary.

        Args:
            data (dict):    input data dictionary.
        """
        points = list(map(Point.from_dict, data["points"]))
        return cls(id=data['id'], name=data['name'], is_vert=data['vert'],
                   radius=data['radius'], track=points)
