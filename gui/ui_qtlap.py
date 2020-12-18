#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize

class UI_QtLapWindow:
    def __init__(self):
        self.window_title = 'QtLap v.0.1'

    def retranslateUi(self, widget):
        widget.setWindowTitle(self.window_title)
    
    def setupUi(self, widget):
        widget.setMinimumSize(QSize(640, 480))

        centralWidget = QWidget(widget) 
        widget.setCentralWidget(centralWidget)   

        gridLayout = QGridLayout(widget)     
        centralWidget.setLayout(gridLayout)  

        title = QLabel("Hello World from PyQt", widget) 
        title.setAlignment(QtCore.Qt.AlignCenter) 
        gridLayout.addWidget(title, 0, 0)

        widget.showMaximized()

        self.retranslateUi(widget)
