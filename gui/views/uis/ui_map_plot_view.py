#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui


class UI_MapPlotView:
    def __init__(self):
        self.__title = ''
        self.__central_widget = None
        self.__grid_layout = None

    def retranslateUi(self, widget):
        pass

    def setupUi(self, widget):
        self.__central_widget = QtWidgets.QtWidget(widget)
        widget.setCentralWidget(self.__central_widget)
