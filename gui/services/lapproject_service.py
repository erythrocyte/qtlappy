"""
model docstring
"""

from PyQt5 import QtWidgets, QtGui, QtCore
from src.models.lapmodel import LapModel
from gui.resources import resources
from gui.models.project_treeview_item_type import ProjectTreeViewItemType


def to_tree_widget_item(model: LapModel) -> QtWidgets.QTreeWidgetItem:
    """
    def docstring
    """

    if model is None:
        return None

    main = __create_item(model.name, ":/project2", None,
                         ProjectTreeViewItemType.PROJECT)
    main.setData(0, QtCore.Qt.UserRole, model)

    # sub items

    # initial data
    init_data = __create_item(
        'Initial data', ':/init_data', main, ProjectTreeViewItemType.INIT_DATA)

    # initial data sub items
    contours = __create_item('Contours', ':/contour',
                             init_data, ProjectTreeViewItemType.INIT_DATA_CONTOURS)
    wells = __create_item('Wells', ':/well', init_data,
                          ProjectTreeViewItemType.INIT_DATA_WELLS)
    wells_geom = __create_item(
        'Geometry', ':/well_geom', wells, ProjectTreeViewItemType.INIT_DATA_WELLS_WELLSGEOM)
    wells_events = __create_item(
        'Events', ':/well_events', wells, ProjectTreeViewItemType.INIT_DATA_WELLS_WELLSEVENT)
    wells_history = __create_item(
        'History', ':/well_history', wells, ProjectTreeViewItemType.INIT_DATA_WELLS_WELLSHISTORY)

    fluid = __create_item('Fuild properties', ':/fluid',
                          init_data, ProjectTreeViewItemType.INIT_DATA_FLUID)
    reservoir = __create_item('Reservoir properties', ':/reservoir_prop',
                              init_data, ProjectTreeViewItemType.INIT_DATA_RESERVOIR)

    # model data
    model_data = __create_item(
        'Model data', ':/model_data', main, ProjectTreeViewItemType.MODEL_DATA)
    grid = __create_item('Grid', ':/grid', model_data,
                         ProjectTreeViewItemType.MODEL_DATA_GRID)
    maps = __create_item('Fields', ':/field', model_data,
                         ProjectTreeViewItemType.MODEL_DATA_MAPS)
    bound_cond = __create_item('Bound conditions', ':/boundary',
                               model_data, ProjectTreeViewItemType.MODEL_DATA_BOUND_CONDITION)

    results = __create_item('Results', ':/results', main,
                            ProjectTreeViewItemType.RESULTS)
    results_map = __create_item(
        'Maps', ':/result_maps', results, ProjectTreeViewItemType.RESULTS_MAPS)
    results_wells = __create_item(
        'Well work', ':/result_wells_work', results, ProjectTreeViewItemType.RESULTS_WELL_WORK)
    results_field = __create_item(
        'Field data', ':/result_field_data', results, ProjectTreeViewItemType.RESULTS_FIELD_DATA)

    return main


def __create_item(text: str, icon_path: str, parent: QtWidgets.QTreeWidgetItem, tp: int) -> QtWidgets.QTreeWidgetItem:
    item = QtWidgets.QTreeWidgetItem(parent)
    item.setText(0, text)
    item.Type = tp

    if icon_path is not '':
        item.setIcon(0, QtGui.QIcon(icon_path))

    return item
