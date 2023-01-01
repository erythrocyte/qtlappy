"""
module description
"""

from PyQt5 import QtWidgets

from gui.views.uis.ui_geomview import UI_GeomView
from gui.views.dialogs.reservoir_size_dialog import ReservoirSizeDialog

from src.models.lapmodel_geom import LapModelGeom


class GeomView(QtWidgets.QWidget, UI_GeomView):
    """
    class description
    """

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setup_ui(self)

    def set_geom(self, geom: LapModelGeom):
        if not geom:
            return

        if geom.frame.isNull():
            # shaw dialog
            frame_dialog = ReservoirSizeDialog(self)
            a = frame_dialog.exec()

            print(a)
