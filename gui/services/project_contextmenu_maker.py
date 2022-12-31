"""
module description
"""

from PyQt5 import QtWidgets, QtGui, QtCore

from src.models.lapmodel import LapModel


class ProjectContextMenuMaker(QtCore.QObject):

    on_delete_model = QtCore.pyqtSignal(QtWidgets.QTreeWidgetItem)
    on_close_model = QtCore.pyqtSignal(QtWidgets.QTreeWidgetItem)

    def __init__(self, item: QtWidgets.QTreeWidgetItem, parent: QtWidgets = None) -> None:
        self.__tree_item = item
        self.__parent = parent
        super().__init__()

    def get_menu(self):
        menu = QtWidgets.QMenu(self.__parent)
        createAction = menu.addAction('Close')
        createAction.triggered.connect(self.__close_model)

        createAction = menu.addAction('Delete')
        createAction.triggered.connect(self.__delete_model)

        return menu

    def __close_model(self):
        self.on_close_model.emit(self.__tree_item)

    def __delete_model(self):
        self.on_delete_model.emit(self.__tree_item)
