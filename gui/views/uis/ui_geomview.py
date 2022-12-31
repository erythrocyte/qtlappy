#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui

from gui.views.mapplotview import MapPlotView


class UI_GeomView:
    def __init__(self):
        self.__layout = QtWidgets.QGridLayout()
        self.__map = MapPlotView()

    def retranslateUi(self, widget):
        pass

    def setup_ui(self, widget):
        widget.setLayout(self.__layout)
        self.__layout.addWidget(self.__map)
