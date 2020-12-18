#!/usr/bin/env python3
#coding: utf-8

import os
import unittest
from laplapy.readers import bound_reader
from laplapy.readers import holes_reader
from laplapy.classes import gridTri2d


class TestGridMethods(unittest.TestCase):
    def test_polygon(self):
        # arrange
        dirname = os.path.realpath('')
        fn = os.path.join(dirname, 'examples/data/rect_hole/boundary.txt')

        # act
        points = bound_reader.read_bound_file(fn)
        gridMaker = gridTri2d.GridTri2D()
        pts, seg = gridMaker._GridTri2D__polygon(points)

        # assert
        self.assertEqual(4, len(pts))
        self.assertEqual(4, len(seg))
        self.assertEqual([3, 0], seg[3])
        self.assertEqual([2, 3], seg[2])
        self.assertEqual([-5, -2], pts[0])


if __name__ == '__main__':
    unittest.main()
