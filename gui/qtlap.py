#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(1, os.path.realpath(''))

from src.lappy.models.settings.global_setts import GlobalSetts
from src.lappy.services.mesh_maker_2d import MeshMaker2D
from src.lappy.models.field import Field
from views.map_plot_view import MapPlotView
from PyQt5 import QtWidgets
from ui_qtlap import UI_QtLapWindow
import triangle as tr
from models.log_level_enum import LogLevelEnum


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

        self.log_message('Test info', LogLevelEnum.info)
        self.log_message('Test error', LogLevelEnum.error)
        self.log_message('Test warning', LogLevelEnum.warning)
        self.log_message('Test debug', LogLevelEnum.debug)

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
