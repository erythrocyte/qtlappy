""""
lap model (data)
"""

from src.models.lapproject import LapProject

class LapModel():
    """
    lap model
    """

    def __init__(self) -> None:
        self.project = LapProject()
        self.name = ''
        self.id = -1