#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from import_lib import *

from models.lap_project_paths import LapProjectPaths
from src.lappy.models.settings.global_setts import GlobalSetts
from src.lappy.services.mesh_maker_2d import MeshMaker2D
from src.lappy.models.field import Field
from views.map_plot_view import MapPlotView
from PyQt5 import QtWidgets, QtGui, QtCore
from ui_qtlap import UI_QtLapWindow
import triangle as tr
from models.log_level_enum import LogLevelEnum
# ===============should be isolated ======
# ========================================


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
        self.save_project_action.triggered.connect(self.__on_save_project)
        self.proj_explorer_tree.customContextMenuRequested.connect(
            self.__prepareProjectItemContextMenu)

    def __on_new_project_create(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Folder')

        if not folderpath:
            return

        lp = LapProjectPaths(folderpath)
        project = QtWidgets.QTreeWidgetItem(self.proj_explorer_tree)
        project.setText(0, f'Project {self.__project_count + 1}')
        project.setFlags(project.flags()
                         | QtCore.Qt.ItemIsTristate
                         | QtCore.Qt.ItemIsUserCheckable)
        project.Type = lp

        bound = QtWidgets.QTreeWidgetItem(project)
        bound.setText(0, 'Bound')
        bound.setDisabled(True)
        bound.Type = 'A'

        wells = QtWidgets.QTreeWidgetItem(project)
        wells.setText(0, 'Wells')
        wells.setDisabled(True)

        grid = QtWidgets.QTreeWidgetItem(project)
        grid.setText(0, 'Grid')
        grid.setDisabled(True)

        fields = QtWidgets.QTreeWidgetItem(project)
        fields.setText(0, 'Field')
        fields.setDisabled(True)

        self.__project_count += 1

    def __on_save_project(self):
        pass

    def __prepareProjectItemContextMenu(self, point):
        # Infos about the node selected.
        index = self.proj_explorer_tree.indexAt(point)

        if not index.isValid():
            return

        item = self.proj_explorer_tree.itemAt(point)
        name = item.text(0)  # The text of the node.
        tp = type(item.Type).__name__
        self.log_message(f'context menu for {name} with type = {tp}',
                         LogLevelEnum.info)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtLapWindow()
    mainWin.show()
    sys.exit(app.exec_())
