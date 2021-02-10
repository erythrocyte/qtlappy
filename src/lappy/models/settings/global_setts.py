#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.lappy.models.settings import common_well_mesh_setts


class GlobalSetts(object):
    def __init__(self):
        self.well = common_well_mesh_setts.CommonWellMeshSettings(5, 10)
