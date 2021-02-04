#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np

from src.lappy.services.hor_well_maker import HorWellMaker
from src.lappy.models.point import Point
from src.lappy.models.well import Well


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

    def test_hor_well_y_const0_n1_hn1(self):
        # arrange
        track = []
        track.append(Point(0.0, 0.0, -1))
        track.append(Point(1.0, 0.0, -1))
        wl = Well(0, 'duduka', False, 0.1, track)
        n1 = 1
        n2 = 1
        hwm = HorWellMaker()

        # act
        pts, seg = hwm.make_real(wl, n1, n2)

        # assert
        self.assertEqual(2 * (n1 + n2), len(pts))
        self.assertEqual(2 * (n1 + n2), len(seg))

    def test_hor_well_y_const0_n1_hn2(self):
        # arrange
        track = []
        track.append(Point(0.0, 0.0, -1))
        track.append(Point(1.0, 0.0, -1))
        wl = Well(0, 'duduka', False, 0.1, track)
        n1 = 1
        n2 = 2
        hwm = HorWellMaker()

        # act
        pts, seg = hwm.make_real(wl, n1, n2)

        # assert
        self.assertEqual(2 * (n1 + n2), len(pts))
        self.assertEqual(2 * (n1 + n2), len(seg))
        self.assertTrue(np.allclose([0.5, -0.1], pts[2]))

    def test_hor_well_y_const0_n2_hn1(self):
        # arrange
        track = []
        track.append(Point(0.0, 0.0, -1))
        track.append(Point(1.0, 0.0, -1))
        wl = Well(0, 'duduka', False, 0.1, track)
        n1 = 2
        n2 = 1
        hwm = HorWellMaker()

        # act
        pts, seg = hwm.make_real(wl, n1, n2)

        # assert
        self.assertEqual(2 * (n1 + n2), len(pts))
        self.assertEqual(2 * (n1 + n2), len(seg))
        self.assertTrue(np.allclose([-0.1, 0.], pts[1]))

    def test_hor_well_y_const0_n10_hn10(self):
        # arrange
        track = []
        track.append(Point(0.0, 0.0, -1))
        track.append(Point(1.0, 0.0, -1))
        wl = Well(0, 'duduka', False, 0.1, track)
        n1 = 10
        n2 = 10
        hwm = HorWellMaker()

        # act
        pts, seg = hwm.make_real(wl, n1, n2)

        # assert
        self.assertEqual(2 * (n1 + n2), len(pts))
        self.assertEqual(2 * (n1 + n2), len(seg))
        self.assertTrue(np.allclose([0.0, -0.1], pts[10]))
        self.assertTrue(np.allclose([-0.1, 0.], pts[5]))
        self.assertTrue(np.allclose([1.1, 0.], pts[25]))

    def test_hor_well_threepoints_anglemore90_n10_hn10(self):
        # arrange
        track = []
        track.append(Point(0.0, 0.0, -1))
        track.append(Point(10.0, 10.0, -1))
        track.append(Point(30, 0.0, -1))
        rw = 1
        wl = Well(0, 'duduka', False, rw, track)
        n1 = 10
        n2 = 10
        hwm = HorWellMaker()

        # act
        pts, seg = hwm.make_real(wl, n1, n2)

        # assert
        self.assertEqual(3 * (n1 + n2), len(pts))
        self.assertEqual(3 * (n1 + n2), len(seg))
        self.assertTrue(np.allclose([0.7071067812, -0.7071067812], pts[0]))
        self.assertTrue(np.allclose([9.83, 10.987], pts[20], rtol=1e-2))

    def test_hor_well_threepoints_angle90_not_suite(self):
        # arrange
        track = []
        track.append(Point(0.0, 0.0, -1))
        track.append(Point(1.0, 1.0, -1))
        track.append(Point(2.0, 0.0, -1))
        wl = Well(0, 'duduka', False, 0.1, track)
        n1 = 10
        n2 = 10
        hwm = HorWellMaker()

        # act
        pts, seg = hwm.make_real(wl, n1, n2)

        # assert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)
