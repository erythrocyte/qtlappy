"""
"""

import sys
import logging
from PyQt5 import QtWidgets, QtCore
from gui.views.qtlapview import QtLapView
from src.services import model_creator_service
from gui.services.logtextedithandler import LogTextEditHandler
from gui.models.loglevelenum import LogLevelEnum


class QtLappy:

    on_create_empty_project = QtCore.pyqtSlot()

    def __init__(self) -> None:
        self.__main_window = None
        self.__models = []
        self.logger = None

        self.__setup()

    def run(self):
        """
        """

        app = QtWidgets.QApplication(sys.argv)
        self.__prepare_qtlap_view()
        self.__connect()
        self.__main_window.show()
        sys.exit(app.exec_())

    # def log_message(self, mess: str, level: LogLevelEnum):
    #     if level is LogLevelEnum.DEBUG:
    #         self.logger.debug(mess)
    #     elif level is LogLevelEnum.ERROR:
    #         self.logger.error(mess)
    #     elif level is LogLevelEnum.WARNING:
    #         self.logger.warning(mess)
    #     elif level is LogLevelEnum.FATAL:
    #         self.logger.fatal(mess)
    #     else:
    #         self.logger.info(mess)

    def __prepare_qtlap_view(self):
        self.__main_window = QtLapView()
        self.__prepare_qtlap_view_logger()

    def __prepare_qtlap_view_logger(self):
        text_editor_handler = LogTextEditHandler(self.__main_window)
        self.logger.addHandler(text_editor_handler)

        self.__main_window.set_logger_viewer_widget(text_editor_handler.widget)

    def __connect(self):
        self.__connect_main_view()

    def __connect_main_view(self):
        self.__main_window.create_empty_project.connect(
            self.__create_empty_project)

    def __create_empty_project(self, folder: str, name: str):
        model = model_creator_service.create(self.__models, name, folder)
        if model is None:
            self.logger.warning('model not created')
            return

        self.__models.append(model)

        self.__main_window.add_project_to_projects_view(model)

    def __setup(self):
        self.__setup_logger()

    def __setup_logger(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler('app.log', 'w')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
