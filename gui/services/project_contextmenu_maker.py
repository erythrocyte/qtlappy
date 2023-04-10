"""
module description
"""

from PyQt5 import QtWidgets, QtCore


class ProjectContextMenuMaker(QtCore.QObject):
    """
    context menu maker
    """

    on_delete_model = QtCore.pyqtSignal(QtWidgets.QTreeWidgetItem)
    on_close_model = QtCore.pyqtSignal(QtWidgets.QTreeWidgetItem)
    on_edit_model = QtCore.pyqtSignal(QtWidgets.QTreeWidgetItem)
    on_clone_model = QtCore.pyqtSignal(QtWidgets.QTreeWidgetItem)

    def __init__(self, item: QtWidgets.QTreeWidgetItem, parent: QtWidgets = None) -> None:
        self.__tree_item = item
        self.__parent = parent
        super().__init__()

    def get_menu(self):
        """
        prepare menu for project node
        """

        menu = QtWidgets.QMenu(self.__parent)
        action = menu.addAction('Close')
        action.triggered.connect(self.__close_model)

        action = menu.addAction('Delete')
        action.triggered.connect(self.__delete_model)

        action = menu.addAction('Edit')
        action.triggered.connect(self.__edit_model)

        action = menu.addAction('Clone')
        action.triggered.connect(self.__clone_model)

        return menu

    def __close_model(self):
        self.on_close_model.emit(self.__tree_item)

    def __delete_model(self):
        self.on_delete_model.emit(self.__tree_item)

    def __edit_model(self):
        self.on_edit_model.emit(self.__tree_item)

    def __clone_model(self):
        self.on_clone_model.emit(self.__tree_item)
