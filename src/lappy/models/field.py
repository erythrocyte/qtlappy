#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from typing import List
from src.lappy.models.bound import Bound
from src.lappy.models.well import Well

class Field(object):
    """
    Field class. Contains information about input geometry: bound and wells.

    Args:
        name (str): field name.
        bound (Bound): domain bound.
        wells (List[Well]): wells.
    """
    def __init__(self, name, bound: Bound, wells: List[Well]):
        self.name = name
        self.bound = bound
        self.wells = wells

    @classmethod
    def create(cls, name: str, bound_file: str, wells_file: str):
        """
        Creates class instance from input json file for bound and wells.

        Args:
            name (str): field name.
            bound_file (str): json file name which contains domain bound data.
            wells_file (str): json file name which contains wells data.
        """
        bound = Bound.from_json(bound_file)
        with open(wells_file, "r", encoding="utf-8") as f:
            fdata = f.read()
            data = json.loads(fdata)
            wells = list(map(Well.from_dict, data["wells"]))
        return cls(name, bound=bound, wells=wells)