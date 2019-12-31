#!/usr/bin/env python3
#coding: utf-8

import unittest
from laplapy.readers import bound_reader


class TestReaderMethods(unittest.TestCase):
    def test_bound_reader(self):
        fn = ''
        bound_reader.read_bound_file(fn)


if __name__ == '__main__':
    unittest.main()
