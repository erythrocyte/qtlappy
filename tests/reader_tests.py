#!/usr/bin/env python3
#coding: utf-8

import unittest
from laplapy.readers import bound_reader


class TestReaderMethods(unittest.TestCase):
    def test_bound_reader_empty_fn(self):
        fn = ''
        bound_reader.read_bound_file(fn)

    def test_rect_hole_boundary(self):
        # arrange
        import os
        dirname = os.path.realpath('')
        fn = os.path.join(dirname, 'examples/rect_hole/boundary.txt')

        # act
        points = bound_reader.read_bound_file(fn)

        # assert
        self.assertEqual(4, len(points))


if __name__ == '__main__':
    unittest.main()
