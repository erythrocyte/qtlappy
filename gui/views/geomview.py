"""
module description
"""

from PyQt5 import QtWidgets
from gui.views.uis.ui_geomview import UI_GeomView


class GeomView(QtWidgets.QWidget, UI_GeomView):
    """
    class description
    """

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setup_ui(self)
