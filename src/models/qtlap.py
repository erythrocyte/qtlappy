"""
"""

import sys
from PyQt5 import QtWidgets, QtCore
from gui.views.qtlapview import QtLapView
from src.models.lapproject import LapProject
from src.services import empty_project_creator_service


class QtLappy:

    on_create_empty_project = QtCore.pyqtSlot()

    def __init__(self) -> None:
        self.__main_window = None
        self.__projects = []

    def run(self):
        """
        """

        app = QtWidgets.QApplication(sys.argv)
        self.__main_window = QtLapView()

        self.__connect()

        self.__main_window.show()
        sys.exit(app.exec_())

    def __connect(self):
        self.__connect_main_view()

    def __connect_main_view(self):
        self.__main_window.create_empty_project.connect(
            self.__create_empty_project)

    def __create_empty_project(self):
        project = empty_project_creator_service.create(self.__projects)
        self.__projects.append(project)

        self.__main_window.add_project_to_projects_view(project)
