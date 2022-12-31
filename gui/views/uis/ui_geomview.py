#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui

from gui.views.mapplotview import MapPlotView
from gui.resources import resources


class UI_GeomView:
    def __init__(self):
        self.__layout = QtWidgets.QGridLayout()
        self.__map = MapPlotView()
        self.__toolbar = QtWidgets.QToolBar()

    def retranslateUi(self, widget):
        pass

    def setup_ui(self, widget):
        widget.setLayout(self.__layout)
        self.__layout.addWidget(self.__toolbar)
        self.__layout.addWidget(self.__map)

        self.__setup_toolbar()

    def __setup_toolbar(self):
        self.__toolbar.setIconSize(QtCore.QSize(24, 24))
        self.__toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.__draw_out_contour = QtWidgets.QAction(
            QtGui.QIcon(":/well_geom"), "text", self)
        self.__draw_out_contour.setStatusTip("Draw out contour on screen")

        self.__toolbar.addAction(self.__draw_out_contour)
