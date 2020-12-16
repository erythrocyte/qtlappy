#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from typing import List
from src.lappy.models.bound import Bound
from src.lappy.models.well import Well

class Field(object):
    def __init__(self, name, bound: Bound, wells: List[Well]):
        self.name = name
        self.bound = bound
        self.wells = wells

    @classmethod
    def create(cls, name: str, bound_file: str, wells_file: str):
        bound = Bound.from_json(bound_file)
        with open(wells_file, "r", encoding="utf-8") as f:
            fdata = f.read()
            data = json.loads(fdata)
            wells = list(map(Well.from_json, data["wells"]))
        return cls(name, bound=bound, wells=wells)