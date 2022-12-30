#!/usr/bin/env python3
# coding: utf-8

import numpy as np


class VertWellMaker(object):
    """
    vertical well bound points and segments maker
    """

    def make(self, well, nw):
        """
        """
        x = well.track[0].x
        y = well.track[0].y
        rw = well.radius
        pts, seg = self.__circle(x, y, nw, rw)

        return [[x, y], pts, seg]

    def __circle(self, x, y, N, R):
        i = np.arange(N)
        theta = i * 2 * np.pi / N
        pts = np.stack([R * np.cos(theta) + x, R * np.sin(theta) + y], axis=1)
        seg = np.stack([i, i + 1], axis=1) % N
        return pts, seg
