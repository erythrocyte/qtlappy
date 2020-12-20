#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class CommonWellMeshSettings(object):
    """
    Well meshing setting class.
    This class includes the settings for
    meshing well bound. It does not specify each well separately

    Args:
        circle_part_seg_count (int):    defines the amount of points on
                                        vertical well bound circle when
                                        meshing.

        hor_part_seg_count (int):       defines the amount of
                                        points on horizontal part of well when
                                        meshing. Note that this
                                        amount is for one segment
                                        (line between two points of track)
                                        of well track.
    """
    def __init__(self, circle_part_seg_count: int, hor_part_seg_count: int):
        self.n_vert = circle_part_seg_count
        self.n_hor = hor_part_seg_count
