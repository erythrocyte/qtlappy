#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from src.lappy.models.field import Field
from src.lappy.services.mesh_maker_2d import MeshMaker2D
from src.lappy.models.settings.global_setts import GlobalSetts
import matplotlib.pyplot as plt
import triangle as tr


def main():
    dirname = os.path.join(os.path.realpath(''), 'examples/data/rect_hole')
    fn_bound = os.path.join(dirname, 'boundary.json')
    fn_wells = os.path.join(dirname, 'wells.json')

    field = Field.create("test_field", fn_bound, fn_wells)
    print("field created")

    setts = GlobalSetts()
    mesh_maker = MeshMaker2D()
    mesh = mesh_maker.triangulate(field, setts)

    ax = plt.axes()
    tr.plot(ax, **mesh)
    ax.get_xaxis().set_visible(True)
    ax.get_yaxis().set_visible(True)
    plt.show()


if __name__ == '__main__':
    main()
