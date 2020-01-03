#!/usr/bin/env python3
#coding: utf-8

import os
import unittest
from laplapy.readers import bound_reader
from laplapy.readers import holes_reader


class TestReaderMethods(unittest.TestCase):
    def test_rect_hole_boundary(self):
        # arrange
        dirname = os.path.realpath('')
        fn = os.path.join(dirname, 'examples/rect_hole/boundary.txt')

        # act
        points = bound_reader.read_bound_file(fn)

        # assert
        self.assertEqual(4, len(points))

    def test_rect_hole_holes(self):
        """

        """
        # arrange
        dirname = os.path.realpath('')
        fn = os.path.join(dirname, 'examples/rect_hole/holes.txt')

        # act
        holes = holes_reader.read_holes_file(fn)

        #assert
        self.assertEqual(2, len(holes))
        self.assertEqual(0.08, holes[0].rw)
        self.assertEqual(0.081, holes[1].rw)


if __name__ == '__main__':
    unittest.main()
