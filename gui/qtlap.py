#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===============should be isolated ======
import sys
import os
sys.path.insert(1, os.path.realpath(''))
# ========================================

from models.log_level_enum import LogLevelEnum
import triangle as tr
from ui_qtlap import UI_QtLapWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from views.map_plot_view import MapPlotView
from src.lappy.models.field import Field
from src.lappy.services.mesh_maker_2d import MeshMaker2D
from src.lappy.models.settings.global_setts import GlobalSetts


class QtLapWindow(QtWidgets.QMainWindow, UI_QtLapWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.testMethod()
        self.__project_count = 0
        self.__connect()

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

    def log_message(self, mess: str, level: LogLevelEnum):
        if level is LogLevelEnum.debug:
            self.logger.debug(mess)
        elif level is LogLevelEnum.error:
            self.logger.error(mess)
        elif level is LogLevelEnum.warning:
            self.logger.warning(mess)
        else:
            self.logger.info(mess)

    def __connect(self):
        self.new_project_action.triggered.connect(self.__on_new_project_create)

    def __on_new_project_create(self):
        t = QtWidgets.QTreeWidgetItem(self.proj_explorer_tree)
        t.setText(0, f'Project {self.__project_count}')
        t.setFlags(t.flags()
                   | QtCore.Qt.ItemIsTristate
                   | QtCore.Qt.ItemIsUserCheckable)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtLapWindow()
    mainWin.show()
    sys.exit(app.exec_())
