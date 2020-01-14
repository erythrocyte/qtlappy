#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
from laplapy.classes import geom


class TestGeomMethods(unittest.TestCase):
    def test_getlinecf_xconst_zero(self):
        x0, x1 = 0.0, 0.0
        y0, y1 = 0.0, 0.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, 0.0)
        self.assertEqual(b, x0)

    def test_getlinefc_xconst_six(self):
        x0, x1 = 6.0, 6.0
        y0, y1 = 0.0, 8.0

        a, b = geom.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, 0.0)
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


