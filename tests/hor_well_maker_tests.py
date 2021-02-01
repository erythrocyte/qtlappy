#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np

from src.lappy.services.hor_well_maker import HorWellMaker
from src.lappy.models.point import Point


class HorWellMakerTest(unittest.TestCase):
    def test_make_thin_horizontal_three_points_n1(self):
        # arrange
        track = []
        track.append(Point(0.0, 0.0, -1))
        track.append(Point(1.0, 0.0, -1))
        track.append(Point(2.0, 0.0, -1))
        hwm = HorWellMaker()
        n = 1

        # act
        pts, seg = hwm.make_thin(track, n)

        # assert
        self.assertEqual(4, len(pts))
        self.assertEqual(4, len(seg))
        self.assertTrue(np.allclose([2., 0.], pts[2]))
        self.assertTrue(np.allclose([3, 0], seg[-1]))

    def test_make_thin_horizontal_three_points_n0(self):
        # arrange
        track = []
        track.append(Point(0.0, 0.0, -1))
        track.append(Point(1.0, 0.0, -1))
        track.append(Point(2.0, 0.0, -1))
        hwm = HorWellMaker()
        n = 0

        # act
        pts, seg = hwm.make_thin(track, n)

        # assert
        self.assertEqual(0, len(pts))
        self.assertEqual(0, len(seg))

    def test_make_thin_horizontal_three_points_nNegative(self):
        # arrange
        track = []
        track.append(Point(0.0, 0.0, -1))
        track.append(Point(1.0, 0.0, -1))
        track.append(Point(2.0, 0.0, -1))
        hwm = HorWellMaker()
        n = -1

        # act
        pts, seg = hwm.make_thin(track, n)

        # assert
        self.assertTrue(np.empty(pts))
        self.assertTrue(np.empty(seg))

    def test_make_thin_horizontal_trackNone_n1(self):
        # arrange
        hwm = HorWellMaker()
        n = 1

        # act
        pts, seg = hwm.make_thin(None, n)

        # assert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)

    def test_make_thin_horizontal_track_nNone(self):
        # arrange
        track = []
        track.append(Point(0.0, 0.0, -1))
        track.append(Point(1.0, 0.0, -1))
        track.append(Point(2.0, 0.0, -1))
        hwm = HorWellMaker()

        # act
        pts, seg = hwm.make_thin(track, None)

        # assert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)
