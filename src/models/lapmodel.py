""""
lap model (data)
"""

from src.models.lapproject import LapProject
from src.models.lapmodel_geom import LapModelGeom


class LapModel():
    """
    lap model
    """

    def __init__(self) -> None:
        self.project = LapProject()
        self.name = ''
        self.id = -1
        self.geom = LapModelGeom()
