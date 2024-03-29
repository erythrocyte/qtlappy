"""
question box dialog viewer;
"""

from PyQt5 import QtWidgets


def positive_answer(parent: QtWidgets, title: str, text: str) -> bool:
    dialog = QtWidgets.QMessageBox.question(parent, title, text)

    return dialog == QtWidgets.QMessageBox.Yes
