#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import math
from src.lappy.services import geom_oper
from src.lappy.models.point import Point


class TestGeomMethods(unittest.TestCase):
    def test_getlinecf_xconst_zero(self):
        x0, x1 = 0.0, 0.0
        y0, y1 = 0.0, 0.0

        a, b = geom_oper.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, None)
        self.assertEqual(b, None)

    def test_getlinefc_xconst_six(self):
        x0, x1 = 6.0, 6.0
        y0, y1 = 0.0, 8.0

        a, b = geom_oper.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, None)
        self.assertEqual(b, x0)

    def test_getlinefc_yconst_zero(self):
        x0, x1 = 4.0, 6.0
        y0, y1 = 0.0, 0.0

        a, b = geom_oper.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, 0.0)
        self.assertEqual(b, y0)

    def test_getlinefc_yconst_six(self):
        x0, x1 = 4.0, 6.0
        y0, y1 = 6.0, 6.0

        a, b = geom_oper.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, 0.0)
        self.assertEqual(b, y0)

    def test_getlinefc_yx(self):
        x0, x1 = 0.0, 6.0
        y0, y1 = 0.0, 6.0

        a, b = geom_oper.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, 1.0)
        self.assertEqual(b, 0.0)

    def test_getlinefc_negyx(self):
        x0, x1 = 0.0, -6.0
        y0, y1 = 0.0, 6.0

        a, b = geom_oper.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, -1.0)
        self.assertEqual(b, 0.0)

    def test_getlinefc_yx_shift_four(self):
        x0, x1 = 4.0, 5.0
        y0, y1 = 0.0, 1.0

        a, b = geom_oper.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, 1.0)
        self.assertEqual(b, -x0)

    def test_getlinefc_some_line(self):
        x0, x1 = 0.0, 4.0
        y0, y1 = 6.0, 0.0

        a, b = geom_oper.get_line_cf(x0, y0, x1, y1)

        self.assertEqual(a, -6.0 / 4.0)
        self.assertEqual(b, 6.0)

    def test_ortholinecf_x0(self):
        x0, x1 = 0.0, 0.0
        y0, y1 = 6.0, 0.0

        a, b = geom_oper.get_line_cf(x0, y0, x1, y1)

        a1, b1 = geom_oper.ortho_line_cf(a, b, x0, y0)

        self.assertEqual(a, None)
        self.assertEqual(b, 0.0)

        self.assertEqual(a1, 0.0)
        self.assertEqual(b1, 6.0)

    def test_ortholinecf_y0(self):
        x0, x1 = 1.0, 2.0
        y0, y1 = 0.0, 0.0

        a, b = geom_oper.get_line_cf(x0, y0, x1, y1)

        a1, b1 = geom_oper.ortho_line_cf(a, b, x0, y0)

        self.assertEqual(a, 0.0)
        self.assertEqual(b, 0.0)

        self.assertEqual(a1, 0.0)
        self.assertEqual(b1, 0.0)

    def test_ortholinecf_valid(self):
        x0, x1 = 0.0, 4.0
        y0, y1 = 8.0, 0.0

        a, b = geom_oper.get_line_cf(x0, y0, x1, y1)

        a1, b1 = geom_oper.ortho_line_cf(a, b, 1.5, 0)

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
        t0, t1 = geom_oper.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, math.pi)
        self.assertEqual(t1, 2 * math.pi)

    def test_get_polyend_circle_angles_x0_left(self):
        # arrange
        a = None
        b = 0.0
        isLeft = True

        # act
        t0, t1 = geom_oper.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, 0.0)
        self.assertEqual(t1, math.pi)

    def test_get_polyend_circle_angles_y0_right(self):
        # arrange
        a = 0.0
        b = 0.0
        isLeft = False

        # act
        t0, t1 = geom_oper.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, 3.0 * math.pi / 2.0)
        self.assertEqual(t1, 5.0 * math.pi / 2.0)

    def test_get_polyend_circle_angles_y0_left(self):
        # arrange
        a = 0.0
        b = 0.0
        isLeft = True

        # act
        t0, t1 = geom_oper.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, math.pi / 2.0)
        self.assertEqual(t1, 3.0 * math.pi / 2.0)

    def test_get_polyend_circle_angles_yx_right(self):
        # arrange
        a = 1.0
        b = 0.0
        isLeft = False

        # act
        t0, t1 = geom_oper.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, 5.0 * math.pi / 4.0)
        self.assertEqual(t1, 9.0 * math.pi / 4.0)

    def test_get_polyend_circle_angles_yx_left(self):
        # arrange
        a = 1.0
        b = 0.0
        isLeft = True

        # act
        t0, t1 = geom_oper.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, math.pi / 4.0)
        self.assertEqual(t1, 5.0 * math.pi / 4.0)

    def test_get_polyend_circle_angles_negyx_right(self):
        # arrange
        a = -1.0
        b = 0.0
        isLeft = False

        # act
        t0, t1 = geom_oper.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, 7.0 * math.pi / 4.0)
        self.assertEqual(t1, 11.0 * math.pi / 4.0)

    def test_get_polyend_circle_angles_negyx_left(self):
        # arrange
        a = -1.0
        b = 0.0
        isLeft = True

        # act
        t0, t1 = geom_oper.get_polyend_circle_angles(a, b, isLeft)

        # assert
        self.assertEqual(t0, 3.0 * math.pi / 4.0)
        self.assertEqual(t1, 7.0 * math.pi / 4.0)

    def test_parallel_line_cf_x0_plus(self):
        # arrange
        a = None
        b = 0.0
        r = 1
        isPlus = True

        # act
        a1, b1 = geom_oper.paral_line_cf(a, b, r, isPlus)

        # assert
        self.assertEqual(a1, a)
        self.assertEqual(b1, r)

    def test_parallel_line_cf_x0_minus(self):
        # arrange
        a = None
        b = 0.0
        r = 1
        isPlus = False

        # act
        a1, b1 = geom_oper.paral_line_cf(a, b, r, isPlus)

        # assert
        self.assertEqual(a1, a)
        self.assertEqual(b1, -r)

    def test_parallel_line_cf_x0_b4_minus(self):
        # arrange
        a = None
        b = 4.0
        r = 1
        isPlus = False

        # act
        a1, b1 = geom_oper.paral_line_cf(a, b, r, isPlus)

        # assert
        self.assertEqual(a1, a)
        self.assertEqual(b1, -r + b)

    def test_parallel_line_cf_y0_plus(self):
        # arrange
        a = 0.0
        b = 0.0
        r = 1
        isPlus = True

        # act
        a1, b1 = geom_oper.paral_line_cf(a, b, r, isPlus)

        # assert
        self.assertEqual(a1, a)
        self.assertEqual(b1, r + b)

    def test_parallel_line_cf_y0_minus(self):
        # arrange
        a = 0.0
        b = 0.0
        r = 1
        isPlus = False

        # act
        a1, b1 = geom_oper.paral_line_cf(a, b, r, isPlus)

        # assert
        self.assertEqual(a1, a)
        self.assertEqual(b1, -r + b)

    def test_parallel_line_cf_yx_minus(self):
        # arrange
        a = 1.0
        b = 0.0
        r = 1
        isPlus = False

        # act
        a1, b1 = geom_oper.paral_line_cf(a, b, r, isPlus)

        # assert
        self.assertEqual(a1, a)
        self.assertEqual(b1, -r * math.sin(math.pi / 4.0) + b)

    def test_parallel_line_cf_yx_plus(self):
        # arrange
        a = 1.0
        b = 0.0
        r = 1
        isPlus = True

        # act
        a1, b1 = geom_oper.paral_line_cf(a, b, r, isPlus)

        # assert
        self.assertEqual(a1, a)
        self.assertEqual(b1, r * math.sin(math.pi / 4.0) + b)

    def test_parallel_line_cf_negyx_minus(self):
        # arrange
        a = -1.0
        b = 0.0
        r = 1
        isPlus = False

        # act
        a1, b1 = geom_oper.paral_line_cf(a, b, r, isPlus)

        # assert
        self.assertEqual(a1, a)
        self.assertEqual(b1, r * math.sin(math.pi / 4.0) + b)

    def test_parallel_line_cf_negyx_plus(self):
        # arrange
        a = -1.0
        b = 0.0
        r = 1
        isPlus = True

        # act
        a1, b1 = geom_oper.paral_line_cf(a, b, r, isPlus)

        # assert
        self.assertEqual(a1, a)
        self.assertEqual(b1, -r * math.sin(math.pi / 4.0) + b)

    def test_intersection_point_parallel_xconst(self):
        # arrange
        a1, b1 = None, 0.0
        a2, b2 = None, 0.0

        # act
        x, y = geom_oper.get_intersect_point(a1, b1, a2, b2)

        # assert
        self.assertEqual(None, x)
        self.assertEqual(None, y)

    def test_intersection_point_parallel_yconst(self):
        # arrange
        a1, b1 = 0.0, 4.0
        a2, b2 = 0.0, 6.0

        # act
        x, y = geom_oper.get_intersect_point(a1, b1, a2, b2)

        # assert
        self.assertEqual(None, x)
        self.assertEqual(None, y)

    def test_intersection_point_xconst_yconst(self):
        # arrange
        a1, b1 = None, 0.0
        a2, b2 = 0.0, 6.0

        # act
        x, y = geom_oper.get_intersect_point(a1, b1, a2, b2)

        # assert
        self.assertEqual(0.0, x)
        self.assertEqual(6.0, y)

    def test_intersection_point_yconst_xconst(self):
        # arrange
        a1, b1 = 0.0, 6.0
        a2, b2 = None, 0.0

        # act
        x, y = geom_oper.get_intersect_point(a1, b1, a2, b2)

        # assert
        self.assertEqual(0.0, x)
        self.assertEqual(6.0, y)

    def test_intersection_point_yx_negyx(self):
        # arrange
        a1, b1 = 1.0, 0.0
        a2, b2 = -1.0, 0.0

        # act
        x, y = geom_oper.get_intersect_point(a1, b1, a2, b2)

        # assert
        self.assertEqual(0.0, x)
        self.assertEqual(0.0, y)

    def test_intersection_point_custom_lines(self):
        # arrange
        x00, x01, y00, y01 = 2.0, 0.0, 0.0, 5.0
        x10, x11, y10, y11 = 1.0, 4.0, 2.5, 6.0
        a1, b1 = geom_oper.get_line_cf(x00, y00, x01, y01)
        a2, b2 = geom_oper.get_line_cf(x10, y10, x11, y11)

        # act
        x, y = geom_oper.get_intersect_point(a1, b1, a2, b2)

        # assert
        self.assertEqual(1.0, x)
        self.assertEqual(2.5, y)

    def test_rotate_point_clockwise_pi(self):
        # arrange
        angle = math.pi
        p0 = Point(1.0, 0.0, -1)
        pc = Point(0.0, 0.0, -1)

        # act
        x, y = geom_oper.rotate_point(p0, pc, angle)

        # assert
        self.assertAlmostEqual(x, -1.0, places=4)
        self.assertAlmostEqual(y, 0.0, places=4)

    def test_rotate_point_clockwise_pi_half(self):
        # arrange
        angle = math.pi / 2.0
        p0 = Point(1.0, 0.0, -1)
        pc = Point(0.0, 0.0, -1)

        # act
        x, y = geom_oper.rotate_point(p0, pc, angle)

        # assert
        self.assertAlmostEqual(x, 0.0, places=4)
        self.assertAlmostEqual(y, 1.0, places=4)
