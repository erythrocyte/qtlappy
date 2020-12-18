#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QMenuBar, QMenu, QToolBar
from PyQt5.QtCore import QSize


class UI_QtLapWindow:
    def __init__(self):
        self.__window_title = 'QtLap v.0.1'
        self.__central_widget = None
        self.__grid_layout = None
        self.menu_bar = None
        self.tool_bar = None

    def retranslateUi(self, widget):
        widget.setWindowTitle(self.__window_title)
        self.status_bar.showMessage('ready')

    def setupUi(self, widget):
        widget.setMinimumSize(QSize(640, 480))

        self.__central_widget = QWidget(widget)
        widget.setCentralWidget(self.__central_widget)

        self.__grid_layout = QGridLayout(widget)
        self.__central_widget.setLayout(self.__grid_layout)

        widget.showMaximized()

        self.__createMenuBar(widget)
        widget.setMenuBar(self.menu_bar)

        self.__createToolBar(widget)
        self.__createStatusBar(widget)

        self.retranslateUi(widget)

    def __createMenuBar(self, widget):
        self.menu_bar = QMenuBar(widget)

        file_menu = QMenu('&File', widget)
        self.menu_bar.addMenu(file_menu)

        help_menu = QMenu('&Help', widget)
        self.menu_bar.addMenu(help_menu)

    def __createToolBar(self, widget):
        self.tool_bar = QToolBar(widget)

    def __createStatusBar(self, widget):
        self.status_bar = widget.statusBar()
