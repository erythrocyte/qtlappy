
from PyQt5 import QtWidgets

from gui.views.dialogs.uis.ui_reservoir_size_dialog import UI_ReservoirSizeDialog


class ReservoirSizeDialog(QtWidgets.QDialog, UI_ReservoirSizeDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setup_ui()
