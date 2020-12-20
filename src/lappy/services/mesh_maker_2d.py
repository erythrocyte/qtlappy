#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import triangle as tr
from src.lappy.models.field import Field
from src.lappy.services import polygon_maker, well_maker


class MeshMaker2D:
    """
    class definition

    """

    def triangulate(self, field: Field, setts):
        """
        definition

        """
        geom = self.__make_geom(field.bound, field.wells, setts)
        # geom = self.__make_geom(field.bound, None, setts)
        mesh = tr.triangulate(geom, 'qpa0.2')

        return mesh

    def __make_geom(self, bound, wells, setts):
        """
        definition

        """
        if bound is None:
            return None

        poly_maker = polygon_maker.PolygonMaker()
        pts_bound, seg_bound = poly_maker.make_polygon(bound)

        pts = np.vstack([pts_bound])
        seg = np.vstack([seg_bound])

        if wells is None:
            A = dict(vertices=pts, segments=seg)
        else:
            wm = well_maker.WellMaker()
            seg_count = len(seg_bound)
            hls = []
            for well in wells:
                if not well.is_vert:
                    continue
                [hlw, ptsw, segw] = wm.make_well(well, setts)
                hls.append(hlw)
                pts = np.vstack([pts, ptsw])
                seg = np.vstack([seg, segw + seg_count])
                seg_count = seg_count + segw.shape[0]

            A = dict(vertices=pts, segments=seg, holes=hls)

        return A
