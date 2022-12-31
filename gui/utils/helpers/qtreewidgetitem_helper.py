"""
module description
"""

from PyQt5 import QtWidgets


def get_item_king(item: QtWidgets.QTreeWidgetItem) -> QtWidgets.QTreeWidgetItem:
    """
    description
    """

    if not item:
        return None

    parent = item.parent

    if not parent:
        return item

    get_item_king(parent)
