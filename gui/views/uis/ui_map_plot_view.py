#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtWidgets, QtCore, QtGui


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class UI_MapPlotView:
    def __init__(self):
        self.__title = ''
        self.__central_widget = None
        self.__layout = None
        self.scene = MplCanvas(self, width=50, height=4, dpi=100)

    def retranslateUi(self, widget):
        pass

    def setupUi(self, widget):
        self.__layout = QtWidgets.QGridLayout()
        widget.setLayout(self.__layout)

        toolbar = NavigationToolbar(self.scene, self)
        self.__layout.addWidget(toolbar)
        self.__layout.addWidget(self.scene)
