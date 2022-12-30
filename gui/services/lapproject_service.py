"""
model docstring
"""

from PyQt5 import QtWidgets, QtGui
from src.models.lapmodel import LapModel
from gui.resources import resources


def to_tree_widget_item(model: LapModel) -> QtWidgets.QTreeWidgetItem:
    """
    def docstring
    """

    if model is None:
        return None

    main = __create_item(model.name, ":/project2", None)

    # sub items

    # initial data
    init_data = __create_item('Initial data', ':/init_data', main)

    # initial data sub items
    contours = __create_item('Contours', ':/contour', init_data)
    wells = __create_item('Wells', ':/well', init_data)
    wells_geom = __create_item('Geometry', ':/well_geom', wells)
    wells_events = __create_item('Events', ':/well_events', wells)
    wells_history = __create_item('History', ':/well_history', wells)

    fluid = __create_item('Fuild properties', ':/fluid', init_data)
    reservoir = __create_item('Reservoir properties', ':/reservoir_prop', init_data)

    # model data
    model_data = __create_item('Model data', ':/model_data', main)
    grid = __create_item('Grid', ':/grid', model_data)
    maps = __create_item('Fields', ':/field', model_data)
    bound_cond = __create_item('Bound conditions', ':/boundary', model_data)

    results = __create_item('Results', ':/results', main)
    results_map = __create_item('Maps', ':/result_maps', results)
    results_wells = __create_item('Well work', ':/result_wells_work', results)
    results_field = __create_item('Field data', ':/result_field_data', results)

    return main


def __create_item(text: str, icon_path: str, parent: QtWidgets.QTreeWidgetItem) -> QtWidgets.QTreeWidgetItem:
    item = QtWidgets.QTreeWidgetItem(parent)
    item.setText(0, text)

    if icon_path is not '':
        item.setIcon(0, QtGui.QIcon(icon_path))

    return item
