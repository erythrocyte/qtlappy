"""
all geom params
"""

from PyQt5 import QtCore

from src.models.contour import Contour


class LapModelGeom:
    def __init__(self) -> None:
        self.frame = QtCore.QRect(0, 0, 0, 0)
        self.out_countour = Contour()
        self.inner_contours = []  # list of Contour
        self.wells = []  # list of WellContour
