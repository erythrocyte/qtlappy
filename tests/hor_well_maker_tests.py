#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from src.lappy.services.hor_well_maker import HorWellMaker
from src.lappy.models.point import Point


class HorWellMakerTest(unittest.TestCase):
    def test_make_thin_horizontal_three_points(self):
        # arrange
        track = []
        track.append(Point(0.0, 0.0, -1))
        track.append(Point(1.0, 0.0, -1))
        track.append(Point(2.0, 0.0, -1))
        hwm = HorWellMaker()

        # act
        pts, seg, tp = hwm.make_thin(track, 1)

        # assert
        self.assertEqual(4, len(pts))
        self.assertEqual(4, len(seg))
