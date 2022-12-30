"""
question box dialog viewer;
"""

from PyQt5 import QtWidgets


def ask_a_question(title: str, text: str) -> bool:
    dialog = QtWidgets.QMessageBox.question(title, text)

    return dialog == QtWidgets.QMessageBox.Yes
