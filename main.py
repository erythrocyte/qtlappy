"""
main file
"""

import sys
from PyQt5 import QtWidgets
from gui.views.qtlapview import QtLapView


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtLapView()
    mainWin.show()
    sys.exit(app.exec_())
