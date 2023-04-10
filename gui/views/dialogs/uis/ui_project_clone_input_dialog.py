"""

module caption: UI for Project clone custom input dialog
date: 10.04.2023
author: erythrocyte
description: ---

"""

from PyQt5 import QtWidgets


class UIProjectCloneInputDialog():
    """
    _summary_
    """

    def __init__(self):
        self.__setup_ui()

    def __setup_ui(self):
        self.layout = QtWidgets.QGridLayout()
