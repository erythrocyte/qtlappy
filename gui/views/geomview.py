"""
module description
"""

from PyQt5 import QtWidgets, QtCore, QtGui

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

    def set_geom(self, geom: LapModelGeom) -> bool:
        if not geom:
            return

        if geom.frame.isNull():
            # shaw dialog
            frame_dialog = ReservoirSizeDialog(self)

            result = frame_dialog.exec()
            if result == QtWidgets.QDialog.Accepted:
                rect = frame_dialog.get_rect()
                if rect:
                    geom.frame = rect
                    x1, y1, x2, y2 = geom.frame.getCoords()
                    self.map.scene.axes.set_xlim(x1, x2)
                    self.map.scene.axes.set_ylim(y1, y2)

                    self.map.scene.fig.tight_layout()
                    return True

        return False
