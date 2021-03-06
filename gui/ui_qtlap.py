#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtWidgets, QtCore, QtGui
import resources
import functools
import prog
from widgets.log_text_editor_handler import LogTextEditHadler
import logging
from models.log_level_enum import LogLevelEnum


class UI_QtLapWindow:
    def __init__(self):
        self.__window_title = f'QtLap v.{ prog.version }'
        self.central_widget = None
        self.__grid_layout = None
        self.menu_bar = None
        self.tool_bar = None
        self.__dock = None
        self.__project_explorer = None
        self.__proj_explorer_tree = None
        self.__message_window = None

    def retranslateUi(self, widget):
        widget.setWindowTitle(self.__window_title)
        self.__aboutqtlap.setText(u'About QtLap')
        self.status_bar.showMessage('ready')

    def setupUi(self, widget):
        widget.setMinimumSize(QtCore.QSize(640, 480))

        self.central_widget = QtWidgets.QTabWidget(widget)
        self.central_widget.document_mode = True
        widget.setCentralWidget(self.central_widget)

        self.__grid_layout = QtWidgets.QGridLayout()
        self.central_widget.setLayout(self.__grid_layout)

        widget.showMaximized()

        self.__createMenuBar(widget)
        widget.setMenuBar(self.menu_bar)

        self.__createToolBar(widget)
        self.__createStatusBar(widget)

        widget.setWindowIcon(QtGui.QIcon(":qtlap"))

        self.__proj_explorer_tree = QtWidgets.QTreeView(widget)
        self.__project_explorer = QtWidgets.QDockWidget('Project explorer',
                                                        widget)
        self.__project_explorer.setWidget(self.__proj_explorer_tree)
        widget.addDockWidget(QtCore.Qt.LeftDockWidgetArea,
                             self.__project_explorer)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        text_editor_handler = LogTextEditHadler(self)
        self.logger.addHandler(text_editor_handler)

        file_handler = logging.FileHandler('app.log', 'w')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)

        self.__message_window = QtWidgets.QDockWidget('Message window', widget)
        self.__message_window.setWidget(text_editor_handler.widget)
        widget.addDockWidget(QtCore.Qt.BottomDockWidgetArea,
                             self.__message_window)

        # self.__main_dock_widget = QtWidgets.QDockWidget('')

        self.retranslateUi(widget)

    def __createMenuBar(self, widget):
        self.menu_bar = QtWidgets.QMenuBar(widget)

        # -- File
        self.__file_menu = QtWidgets.QMenu('&File', widget)
        self.menu_bar.addMenu(self.__file_menu)

        self.__close_action = QtWidgets.QAction(QtGui.QIcon(":power_off"),
                                                '&Close', widget)
        self.__close_action.triggered.connect(widget.close)
        self.__file_menu.addAction(self.__close_action)

        # -- View
        self.__view_menu = QtWidgets.QMenu('&View', widget)
        self.menu_bar.addMenu(self.__view_menu)

        self.__view_obj_browser_action = QtWidgets.QAction('&Project explorer',
                                                           widget)
        self.__view_obj_browser_action.triggered.connect(
            self.__visible_obj_browser)
        self.__view_menu.addAction(self.__view_obj_browser_action)

        self.__view_message_widget_action = QtWidgets.QAction('&Messages',
                                                              widget)
        self.__view_message_widget_action.triggered.connect(
            self.__view_message)
        self.__view_menu.addAction(self.__view_message_widget_action)

        # --- Help
        self.__help_menu = QtWidgets.QMenu('&Help', widget)
        self.menu_bar.addMenu(self.__help_menu)

        self.__aboutqtlap = QtWidgets.QAction('About QtLap', widget)
        self.__aboutqtlap.triggered.connect(functools.partial(
            QtWidgets.QMessageBox.about,
            widget,
            'About QtLap',
            """
            < b > Laplace equation solver and visualizer < /b >
            < br >< br > Version {0} <br><br>
            <a href="http://{1}/releases/latest">{1}</a>
            """.format(prog.version, "www.github.com/erythrocyte/qtlappy/")))
        self.__help_menu.addAction(self.__aboutqtlap)
        self.__aboutqt = QtWidgets.QAction('About Qt', widget)
        self.__aboutqt.triggered.connect(QtWidgets.QApplication.aboutQt)
        self.__help_menu.addAction(self.__aboutqt)

    def __createToolBar(self, widget):
        self.tool_bar = QtWidgets.QToolBar(widget)

    def __createStatusBar(self, widget):
        self.status_bar = widget.statusBar()

    def __visible_obj_browser(self):
        self.__project_explorer.setVisible(True)

    def __view_message(self):
        self.__message_window.setVisible(True)

    def log_message(self, mess: str, level: LogLevelEnum):
        if level is LogLevelEnum.debug:
            self.logger.debug(mess)
        elif level is LogLevelEnum.error:
            self.logger.error(mess)
        elif level is LogLevelEnum.warning:
            self.logger.warning(mess)
        else:
            self.logger.info(mess)
