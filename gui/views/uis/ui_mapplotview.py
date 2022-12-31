#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui

import sys
import matplotlib

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from gui.views.widgets.mpl_canvas import MplCanvas


class UI_MapPlotView:
    def __init__(self):
        self.__title = ''
        self.__central_widget = None
        self.__layout = None
        self.scene = MplCanvas(self, width=50, height=4, dpi=100)
        self.toolbar = None

    def retranslateUi(self, widget):
        pass

    def setupUi(self, widget):
        self.__layout = QtWidgets.QGridLayout()
        widget.setLayout(self.__layout)

        self.toolbar = NavigationToolbar(self.scene, self)
        self.__layout.addWidget(self.toolbar)
        self.__layout.addWidget(self.scene)
