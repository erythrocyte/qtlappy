#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from src.lappy.models.point import Point


class Bound(object):
    def __init__(self, name, points):
        self.name = name
        self.points = points

    @classmethod
    def from_json(cls, json_file_name):
        with open(json_file_name, "r", encoding="utf-8") as f:
            fdata = f.read()
            data = json.loads(fdata)["bound"]
            name = data["name"]
            points = list(map(Point.from_json, data["points"]))
            return cls(name, points)
