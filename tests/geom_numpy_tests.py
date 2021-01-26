#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.lappy.models.point import Point
from src.lappy.services import geom_numpy


class TestGeomNumpy(unittest.TestCase):
    def test_line_two_points_usefirst_uselast_nodivision(self):
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
        self.assertAlmostEqual(0.0, pts[0][0])

    def test_line_two_points_usefirst_uselast_n10(self):
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
