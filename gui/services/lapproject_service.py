"""
"""

from PyQt5 import QtWidgets, QtGui
from src.models.lapproject import LapProject


def to_tree_widget_item(project: LapProject) -> QtWidgets.QTreeWidgetItem:
    if project is None:
        return None

    main = __create_item(project.name, ":project", None)

    # sub items

    # initial data
    init_data = __create_item('Initial data', '', main)

    # initial data sub items
    contours = __create_item('Contours', '', init_data)
    wells = __create_item('Wells', '', init_data)
    wells_geom = __create_item('Geometry', '', wells)
    wells_events = __create_item('Events', '', wells)
    wells_history = __create_item('History', '', wells)

    fluid = __create_item('Fuild properties', '', init_data)
    reservoir = __create_item('Reservoir properties', '', init_data)

    # model data
    model_data = __create_item('Model data', '', main)
    grid = __create_item('Grid', '', model_data)
    maps = __create_item('Fields', '', model_data)
    bound_cond = __create_item('Bound conditions', '', model_data)

    results = __create_item('Results', '', main)

    return main


def __create_item(text: str, icon_path: str, parent: QtWidgets.QTreeWidgetItem) -> QtWidgets.QTreeWidgetItem:
    item = QtWidgets.QTreeWidgetItem(parent)
    item.setText(0, text)

    if icon_path is not '':
        item.setIcon(0, QtGui.QIcon(icon_path))

    return item
