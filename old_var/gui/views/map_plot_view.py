#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from gui.views.uis.ui_map_plot_view import UI_MapPlotView


class MapPlotView(QtWidgets.QWidget, UI_MapPlotView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
