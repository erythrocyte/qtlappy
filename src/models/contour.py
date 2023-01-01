"""
contour
"""


from src.models.contour_display_settings import ContourDisplaySetts


class Contour:
    def __init__(self) -> None:
        self.name = ''
        self.id = -1
        self.points = []  # List[QtGui.QVector2D]
        self.display_setts = ContourDisplaySetts()
