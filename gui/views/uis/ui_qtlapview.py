"""
main view user interface definition
"""

import functools
import logging
from PyQt5 import QtWidgets, QtCore, QtGui
from gui import prog
from gui.services.logtextedithandler import LogTextEditHandler
from gui.resources import resources


class UIQtLapView:
    """
    ui for qt lap view
    """

    def __init__(self):
        self.__window_title = f'QtLap v.{ prog.VERSION }'
        self.central_widget = None
        self.__grid_layout = None
        self.menu_bar = None
        self.tool_bar = None
        # self.__dock = None
        self.__project_explorer = None
        self.__message_window = None
        self.proj_explorer_tree = None
        self.logger = None

    def retranslate_ui(self, widget):
        widget.setWindowTitle(self.__window_title)
        self.__aboutqtlap.setText(u'About QtLap')
        self.status_bar.showMessage('ready')

    def setup_ui(self, widget):
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

        widget.setWindowIcon(QtGui.QIcon(":/qtlap"))

        self.__createProjectWindow(widget)
        self.__createMessageWindow(widget)

        self.retranslate_ui(widget)

    def __createProjectWindow(self, widget):
        self.proj_explorer_tree = QtWidgets.QTreeWidget(widget)
        self.proj_explorer_tree.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.proj_explorer_tree.setHeaderHidden(True)
        self.__project_explorer = QtWidgets.QDockWidget('Project explorer',
                                                        widget)
        self.__project_explorer.setWidget(self.proj_explorer_tree)
        widget.addDockWidget(QtCore.Qt.LeftDockWidgetArea,
                             self.__project_explorer)

    def __createMessageWindow(self, widget):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        text_editor_handler = LogTextEditHandler(self)
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

    def __createMenuBar(self, widget):
        self.menu_bar = QtWidgets.QMenuBar(widget)

        # -- File
        self.__menuBarFile(widget)

        # -- View
        self.__menuBarView(widget)

        # -- Project
        self.__menuBarProject(widget)

        # --- Help
        self.__menuBarHelp(widget)

    def __menuBarFile(self, widget):
        self.__file_menu = QtWidgets.QMenu('&File', widget)
        self.menu_bar.addMenu(self.__file_menu)

        self.__close_action = QtWidgets.QAction(QtGui.QIcon(":/power_off"),
                                                '&Close', widget)
        self.__close_action.triggered.connect(widget.close)
        self.__file_menu.addAction(self.__close_action)

    def __menuBarView(self, widget):
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

    def __menuBarProject(self, widget):
        self.__project_menu = QtWidgets.QMenu('&Project', widget)
        self.menu_bar.addMenu(self.__project_menu)

        self.new_project_action = QtWidgets.QAction('&New', widget)
        self.__project_menu.addAction(self.new_project_action)

        self.open_project_action = QtWidgets.QAction('&Open', widget)
        self.__project_menu.addAction(self.open_project_action)

        self.save_project_action = QtWidgets.QAction('&Save', widget)
        self.__project_menu.addAction(self.save_project_action)

        # self.open_project_action = QtWidgets.QAction('&Delete', widget)
        # self.__project_menu.addAction(self.open_project_action)

    def __menuBarHelp(self, widget):
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
            """.format(prog.VERSION, "www.github.com/erythrocyte/qtlappy/")))
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
