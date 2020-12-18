#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from ui_qtlap import UI_QtLapWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

class QtLapWindow(QMainWindow, UI_QtLapWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI_QtLapWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtLapWindow()
    mainWin.show()
    sys.exit( app.exec_() )
        
