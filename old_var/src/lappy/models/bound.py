#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from typing import List
from src.lappy.models.point import Point


class Bound(object):
    """
    Domain bound class.

    Args:
        name (str): bound name.        
        points (List[Point]): bound points.
    """
    def __init__(self, name: str, points: List[Point]):
        self.name = name
        self.points = points

    @classmethod
    def from_json(cls, json_file_name: str):
        """
        Creates class instance from json file.

        Args:
            json_file_name (str): json file name which contains domain bound data.
        """
        with open(json_file_name, "r", encoding="utf-8") as f:
            fdata = f.read()
            data = json.loads(fdata)["bound"]
            points = list(map(Point.from_dict, data["points"]))
            return cls(data["name"], points)
