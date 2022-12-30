"""
qt lappy main view
"""

from gui import prog
from PyQt5 import QtWidgets, QtGui, QtCore
from gui.views.uis.ui_qtlapview import UIQtLapView
from src.models.lapmodel import LapModel
from gui.services import lapproject_service
from gui.models.loglevelenum import LogLevelEnum


class QtLapView(QtWidgets.QMainWindow, UIQtLapView):
    """
    view
    """

    create_empty_project = QtCore.pyqtSignal(str, str)
    log_message = QtCore.pyqtSignal(str, LogLevelEnum)

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup_ui(self)
        self.__connect()
        self.__readSettings()

    def add_tab(self, widget: QtWidgets.QWidget, name: str):
        """
        add tab to pages
        """
        self.central_widget.addTab(widget, name)

    def add_project_to_projects_view(self, model: LapModel):
        item = lapproject_service.to_tree_widget_item(model)
        if item is not None:
            self.proj_explorer_tree.addTopLevelItem(item)

    def __connect(self):
        self.new_project_action.triggered.connect(self.__on_new_project_create)
        self.save_project_action.triggered.connect(self.__on_save_project)
        self.proj_explorer_tree.customContextMenuRequested.connect(
            self.__prepareProjectItemContextMenu)

    def __on_new_project_create(self):
        last_dir = self.settings.value('new_project_last_dir')
        last_dir = '' if last_dir is None else last_dir
        project_folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Folder', last_dir)

        if not project_folder:
            return

        self.settings.setValue('new_project_last_dir', project_folder)

        input = QtWidgets.QInputDialog()
        input.setWhatsThis('test')

        project_name, status = input.getText(
            self, 'Project name', 'Please, insert project name')

        if not status:
            return

        self.create_empty_project.emit(project_folder, project_name)

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

    def __readSettings(self):
        self.settings = QtCore.QSettings(prog.ORGANIZATION, prog.PRODUCT_NAME)
