
from PyQt5 import QtWidgets, QtCore

from gui.views.dialogs.uis.ui_reservoir_size_dialog import UI_ReservoirSizeDialog


class ReservoirSizeDialog(QtWidgets.QDialog, UI_ReservoirSizeDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setup_ui(self)
        self.setModal(True)

    def get_rect(self) -> QtCore.QRect:
        x1 = self.x0val.value()
        y1 = self.y0val.value()

        x2 = self.x1val.value()
        y2 = self.y1val.value()
        rect = QtCore.QRect(x1, y1, x2, y2)

        return rect
