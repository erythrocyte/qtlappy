"""
module docstting
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
from PyQt5 import QtWidgets


class LogTextEditHadler(logging.Handler):
    """
    Doc string
    """

    def __init__(self, parent):
        super().__init__()
        self.widget = QtWidgets.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)
        self.setLevel(logging.INFO)
        self.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            '%Y-%m-%d %H:%M:%S'))

    def emit(self, record):
        frmt_msg = self.format(record)
        msg = self.beatify_message(frmt_msg, record.levelname)
        self.widget.appendHtml(msg)

    def beatify_message(self, msg: str, log_level: str):
        if log_level == 'WARNING':
            return f'<font color=\"Orange\">{msg}</font>'
        elif log_level == 'ERROR':
            return f'<font color=\"Red\">{msg}</font>'
        else:
            return msg
