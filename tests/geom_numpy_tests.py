#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy.testing as nptest
import numpy as np

from src.lappy.models.point import Point
from src.lappy.services import geom_numpy


class TestGeomNumpy(unittest.TestCase):
    def test_line_usefirst_uselast_n1(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(1.0, 0.0, -1)
        n = 1

        # act
        pts, seg = geom_numpy.line(p0, p1, n, use_first_pt=True,
                                   use_last_pt=True)

        # asssert
        self.assertEqual(n+1, len(pts))
        self.assertEqual(n, len(seg))
        self.assertTrue(np.array_equal(np.array([0.0, 0.0]), pts[0],
                                       equal_nan=True))

    def test_line_notusefirst_uselast_n1(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(1.0, 0.0, -1)
        n = 1

        # act
        pts, seg = geom_numpy.line(p0, p1, n, use_first_pt=False,
                                   use_last_pt=True)

        # asssert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)

    def test_line_usefirst_notuselast_n1(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(1.0, 0.0, -1)
        n = 1

        # act
        pts, seg = geom_numpy.line(p0, p1, n,
                                   use_first_pt=True,
                                   use_last_pt=False)

        # asssert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)

    def test_line_notusefirst_notuselast_n1(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(1.0, 0.0, -1)
        n = 1

        # act
        pts, seg = geom_numpy.line(p0, p1, n,
                                   use_first_pt=False,
                                   use_last_pt=False)

        # asssert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)

    def test_line_usefirst_uselast_n10(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(1.0, 0.0, -1)
        n = 10

        # act
        pts, seg = geom_numpy.line(p0, p1, n, use_first_pt=True,
                                   use_last_pt=True)

        # asssert
        self.assertEqual(n+1, len(pts))
        self.assertEqual(n, len(seg))
        self.assertTrue(np.array_equal(np.array([0.5, 0.0]), pts[5],
                                       equal_nan=True))

    def test_line_notusefirst_uselast_n10(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(1.0, 0.0, -1)
        n = 10

        # act
        pts, seg = geom_numpy.line(p0, p1, n,
                                   use_first_pt=False,
                                   use_last_pt=True)

        # asssert
        self.assertEqual(n, len(pts))
        self.assertEqual(n-1, len(seg))
        self.assertTrue(np.array_equal(np.array([0.1, 0.0]), pts[0],
                                       equal_nan=True))

    def test_line_usefirst_notuselast_n10(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(1.0, 0.0, -1)
        n = 10

        # act
        pts, seg = geom_numpy.line(p0, p1, n,
                                   use_first_pt=True,
                                   use_last_pt=False)

        # asssert
        self.assertEqual(n, len(pts))
        self.assertEqual(n-1, len(seg))
        self.assertTrue(np.array_equal(np.array([0.9, 0.0]), pts[-1],
                                       equal_nan=True))

    def test_line_usefirst_uselast_n0(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(1.0, 0.0, -1)
        n = 0

        # act
        pts, seg = geom_numpy.line(p0, p1, n, use_first_pt=True,
                                   use_last_pt=True)

        # asssert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)

    def test_line_notusefirst_uselast_n0(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(1.0, 0.0, -1)
        n = 0

        # act
        pts, seg = geom_numpy.line(p0, p1, n,
                                   use_first_pt=False,
                                   use_last_pt=True)

        # asssert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)

    def test_line_usefirst_notuselast_n0(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(1.0, 0.0, -1)
        n = 0

        # act
        pts, seg = geom_numpy.line(p0, p1, n,
                                   use_first_pt=True,
                                   use_last_pt=False)

        # asssert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)

    def test_line_samepoints_usefirst_uselast_n10(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(0.0, 0.0, -1)
        n = 10

        # act
        pts, seg = geom_numpy.line(p0, p1, n,
                                   use_first_pt=True,
                                   use_last_pt=True)

        # asssert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)

    def test_line_samepoints_usefirst_uselast_nNone(self):
        # arrange
        p0 = Point(0.0, 0.0, -1)
        p1 = Point(0.0, 0.0, -1)
        n = None

        # act
        pts, seg = geom_numpy.line(p0, p1, n,
                                   use_first_pt=True,
                                   use_last_pt=True)

        # asssert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)

    def test_sector_usefirstpt_uselastpt_n1(self):
        # arrange
        p0 = Point(-1., 0., -1)
        pc = Point(0., 0., -1)
        n = 1
        clockwise = True

        # act
        pts, seg = geom_numpy.sector(p0, pc, n, clockwise,
                                     use_first_pt=True,
                                     use_last_pt=True)

        # assert
        self.assertEqual(n+1, len(pts))
        self.assertEqual(n, len(seg))
        self.assertTrue(np.array_equal(np.array([0, 1]), seg[0],
                                       equal_nan=True))

    def test_sector_notusefirstpt_uselastpt_n1(self):
        # arrange
        p0 = Point(-1., 0., -1)
        pc = Point(0., 0., -1)
        n = 1
        clockwise = True

        # act
        pts, seg = geom_numpy.sector(p0, pc, n, clockwise,
                                     use_first_pt=False,
                                     use_last_pt=True)

        # assert
        self.assertEqual(None, pts)
        self.assertEqual(None, seg)
