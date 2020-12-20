#!/usr/bin/env python3
# coding: utf-8

from src.lappy.models import well
from src.lappy.models.settings import global_setts
from src.lappy.services.vert_well_maker import VertWellMaker
from src.lappy.services.hor_well_maker import HorWellMaker


class WellMaker(object):
    """
    well points and segments maker class
    """
    def __init__(self):
        self.vert_well_maker = VertWellMaker()
        self.hor_well_maker = HorWellMaker()

    def make_well(self, well: well.Well, setts: global_setts.GlobalSetts):
        """

        """

        nw = setts.well.n_vert
        hnw = setts.well.n_hor
        if well.is_vert:
            [hl, pts, seg] = self.vert_well_maker.make(well, nw)
        else:
            [hl, pts, seg] = self.hor_well_maker.make(well, nw, hnw)
        return [hl, pts, seg]
