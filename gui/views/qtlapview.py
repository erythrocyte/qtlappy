"""
qt lappy main view
"""

from PyQt5 import QtWidgets, QtGui
from gui.views.uis.ui_qtlapview import UIQtLapView
from gui.models.loglevelenum import LogLevelEnum


class QtLapView(QtWidgets.QMainWindow, UIQtLapView):
    """
    view
    """

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup_ui(self)
        self.__connect()

    def add_tab(self, widget: QtWidgets.QWidget, name: str):
        """
        add tab to pages
        """
        self.central_widget.addTab(widget, name)

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

        # lp = LapProjectPaths(folderpath)
        # project = QtWidgets.QTreeWidgetItem(self.proj_explorer_tree)
        # project.setText(0, f'Project {self.__project_count + 1}')
        # project.setFlags(project.flags()
        #                  | QtCore.Qt.ItemIsTristate
        #                  | QtCore.Qt.ItemIsUserCheckable)
        # project.Type = lp

        # bound = QtWidgets.QTreeWidgetItem(project)
        # bound.setText(0, 'Bound')
        # bound.setDisabled(True)
        # bound.Type = ProjectItemType.BOUND

        # wells = QtWidgets.QTreeWidgetItem(project)
        # wells.setText(0, 'Wells')
        # wells.setDisabled(True)
        # wells.Type = ProjectItemType.WELL

        # grid = QtWidgets.QTreeWidgetItem(project)
        # grid.setText(0, 'Grid')
        # grid.setDisabled(True)
        # grid.Type = ProjectItemType.GRID

        # # fields = QtWidgets.QTreeWidgetItem(project)
        # # fields.setText(0, 'Field')
        # # fields.setDisabled(True)
        # # fields.Type = ProjectItemType.FIELD

        # self.__project_count += 1

    def __on_save_project(self):
        pass

    def __prepareProjectItemContextMenu(self, point):
        # Infos about the node selected.
        index = self.proj_explorer_tree.indexAt(point)

        if not index.isValid():
            return

        # item = self.proj_explorer_tree.itemAt(point)
        # name = item.text(0)  # The text of the node.
        # tp = item.Type  # type(item.Type) //.__name__

        # if tp == ProjectItemType.BOUND:
        #     self.__boundContextMenu()

        # self.log_message(f'context menu for {name} with type = {tp}',
        #                  LogLevelEnum.info)

    # def __boundContextMenu(self):
    #     menu = QtWidgets.QMenu(self)
    #     createAction = menu.addAction('Create')
    #     createAction.triggered.connect(self.__createBound)
    #     menu.popup(QtGui.QCursor.pos())
