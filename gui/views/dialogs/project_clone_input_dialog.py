
from PyQt5 import QtWidgets, QtCore

from gui.views.dialogs.uis.ui_project_clone_input_dialog import UIProjectCloneInputDialog


class ProjectCloneInputDialog(QtWidgets.QDialog, UIProjectCloneInputDialog):
    """
    _summary_

    Args:
        QtWidgets (_type_): _description_
        UIProjectCloneInputDialog (_type_): _description_
    """

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setLayout(self.layout)
        self.setModal(True)
