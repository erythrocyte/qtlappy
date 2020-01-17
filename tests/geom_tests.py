#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import math
from laplapy.classes import geom


class TestGeomMethods(unittest.TestCase):
    def test_getlinecf_xconst_zero(self):
        x0, x1 = 0.0, 0.0
        y0, y1 = 0.0, 0.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, None)
        self.assertEqual(b, None)

    def test_getlinefc_xconst_six(self):
        x0, x1 = 6.0, 6.0
        y0, y1 = 0.0, 8.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, None)
        self.assertEqual(b, x0)

    def test_getlinefc_yconst_zero(self):
        x0, x1 = 4.0, 6.0
        y0, y1 = 0.0, 0.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, 0.0)
        self.assertEqual(b, y0)

    def test_getlinefc_yconst_six(self):
        x0, x1 = 4.0, 6.0
        y0, y1 = 6.0, 6.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, 0.0)
        self.assertEqual(b, y0)

    def test_getlinefc_yx(self):
        x0, x1 = 0.0, 6.0
        y0, y1 = 0.0, 6.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, 1.0)
        self.assertEqual(b, 0.0)

    def test_getlinefc_yx(self):
        x0, x1 = 0.0, -6.0
        y0, y1 = 0.0, 6.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, -1.0)
        self.assertEqual(b, 0.0)

    def test_getlinefc_yx_shift_four(self):
        x0, x1 = 4.0, 5.0
        y0, y1 = 0.0, 1.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, 1.0)
        self.assertEqual(b, -x0)

    def test_getlinefc_some_line(self):
        x0, x1 = 0.0, 4.0
        y0, y1 = 6.0, 0.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, -6.0 / 4.0)
        self.assertEqual(b, 6.0)


    def test_ortholinecf_x0(self):
        x0, x1 = 0.0, 0.0
        y0, y1 = 6.0, 0.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        a1, b1 = geom.ortho_line_cf(a, b, x0, y0)

        self.assertEqual(a, None)
        self.assertEqual(b, 0.0)

        self.assertEqual(a1, 0.0)
        self.assertEqual(b1, 6.0)

    def test_ortholinecf_y0(self):
        x0, x1 = 1.0, 2.0
        y0, y1 = 0.0, 0.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        a1, b1 = geom.ortho_line_cf(a, b, x0, y0)

        self.assertEqual(a, 0.0)
        self.assertEqual(b, 0.0)

        self.assertEqual(a1, 0.0)
        self.assertEqual(b1, 0.0)

    def test_ortholinecf_valid(self):
        x0, x1 = 0.0, 4.0
        y0, y1 = 8.0, 0.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        a1, b1 = geom.ortho_line_cf(a, b, 1.5, 0)

        self.assertEqual(a, -2.0)
        self.assertEqual(b, 8.0)

        self.assertEqual(a1, 1.0 / 2.0)
        self.assertEqual(b1, -3.0 / 4.0)

    def test_get_polyend_circle_angles_x0_right(self):
        # arrange
        a = None
        b = 0.0
        isLeft = False

        # act
        t0, t1 = geom.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, math.pi)
        self.assertEqual(t1, 2 * math.pi)

    def test_get_polyend_circle_angles_x0_left(self):
        # arrange
        a = None
        b = 0.0
        isLeft = True

        # act
        t0, t1 = geom.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, 0.0)
        self.assertEqual(t1, math.pi)

    def test_get_polyend_circle_angles_y0_right(self):
        # arrange
        a = 0.0
        b = 0.0
        isLeft = False

        # act
        t0, t1 = geom.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, 3.0 * math.pi / 2.0)
        self.assertEqual(t1, 5.0 * math.pi / 2.0)

    def test_get_polyend_circle_angles_y0_left(self):
        # arrange
        a = 0.0
        b = 0.0
        isLeft = True

        # act
        t0, t1 = geom.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, math.pi/ 2.0)
        self.assertEqual(t1, 3.0 * math.pi / 2.0)

    def test_get_polyend_circle_angles_yx_right(self):
        # arrange
        a = 1.0
        b = 0.0
        isLeft = False

        # act
        t0, t1 = geom.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, 5.0 * math.pi / 4.0)
        self.assertEqual(t1, 9.0 * math.pi / 4.0)

    def test_get_polyend_circle_angles_yx_left(self):
        # arrange
        a = 1.0
        b = 0.0
        isLeft = True

        # act
        t0, t1 = geom.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, math.pi / 4.0)
        self.assertEqual(t1, 5.0 * math.pi / 4.0)

    def test_get_polyend_circle_angles_negyx_right(self):
        # arrange
        a = -1.0
        b = 0.0
        isLeft = False

        # act
        t0, t1 = geom.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, 7.0 * math.pi / 4.0)
        self.assertEqual(t1, 11.0 * math.pi / 4.0)

    def test_get_polyend_circle_angles_negyx_left(self):
        # arrange
        a = -1.0
        b = 0.0
        isLeft = True

        # act
        t0, t1 = geom.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, 3.0 * math.pi / 4.0)
        self.assertEqual(t1, 7.0 * math.pi / 4.0)





