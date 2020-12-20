#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.lappy.models.settings.common_well_mesh_setts import CommonWellMeshSettings


class GlobalSetts(object):
    def __init__(self):
        self.well = CommonWellMeshSettings(10, 10)
