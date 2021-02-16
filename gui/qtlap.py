#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(1, os.path.realpath(''))

## do not change
from src.lappy.models.settings.global_setts import GlobalSetts
from src.lappy.services.mesh_maker_2d import MeshMaker2D
from src.lappy.models.field import Field
from views.map_plot_view import MapPlotView
from PyQt5 import QtWidgets
from ui_qtlap import UI_QtLapWindow
import triangle as tr


class QtLapWindow(QtWidgets.QMainWindow, UI_QtLapWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.testMethod()

    def addTab(self, widget: QtWidgets.QWidget):
        self.central_widget.addTab(widget, "Test")

    def testMethod(self):
        mp = MapPlotView()

        dirname = os.path.join(os.path.realpath(''), 'examples/data/rect_hole')
        fn_bound = os.path.join(dirname, 'boundary.json')
        fn_wells = os.path.join(dirname, 'wells.json')
        field = Field.create("test_field", fn_bound, fn_wells)

        setts = GlobalSetts()
        mesh_maker = MeshMaker2D()
        mesh = mesh_maker.triangulate(field, setts)

        ax = mp.scene.axes
        tr.plot(ax, **mesh)
        self.addTab(mp)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtLapWindow()
    mainWin.show()
    sys.exit(app.exec_())
