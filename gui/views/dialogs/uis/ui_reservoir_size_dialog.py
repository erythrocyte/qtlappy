from PyQt5 import QtWidgets


class UI_ReservoirSizeDialog():
    """
    """

    def __init__(self) -> None:
        """
        """

        self.__x0label = QtWidgets.QLabel(self)
        self.__y0label = QtWidgets.QLabel(self)
        self.__x1label = QtWidgets.QLabel(self)
        self.__y1label = QtWidgets.QLabel(self)

        self.x0val = QtWidgets.QDoubleSpinBox(self)
        self.y0val = QtWidgets.QDoubleSpinBox(self)
        self.x1val = QtWidgets.QDoubleSpinBox(self)
        self.y1val = QtWidgets.QDoubleSpinBox(self)

        self.__layout = QtWidgets.QGridLayout(self)

        self.__btn_ok = QtWidgets.QPushButton(self)
        self.__btn_cancel = QtWidgets.QPushButton(self)

    def retranslate_ui(self, widget: QtWidgets.QDialog):
        """
        """

        self.__x0label.setText("x0")
        self.__x0label.setToolTip("Left upper point of rectangle")

        self.__y0label.setText("y0")
        self.__y0label.setToolTip("Left upper point of rectangle")

        self.__x1label.setText("x1")
        self.__x1label.setToolTip("Right down point of rectangle")

        self.__y1label.setText("y1")
        self.__y1label.setToolTip("Right down point of rectangle")

        self.__btn_ok.setText("Ok")
        self.__btn_ok.setToolTip("Aplly this")

        self.__btn_cancel.setText("Cancel")
        self.__btn_cancel.setToolTip("Cancel")

        widget.setWindowTitle('Insert task frame size')

    def setup_ui(self, widget: QtWidgets.QWidget):
        """
        _summary_

        Args:
            widget (QtWidgets.QWidget): _description_
        """

        widget.setLayout(self.__layout)

        self.__layout.addWidget(self.__x0label, 0, 0)
        self.__layout.addWidget(self.x0val, 0, 1)

        self.__layout.addWidget(self.__y0label, 0, 2)
        self.__layout.addWidget(self.y0val, 0, 3)

        self.__layout.addWidget(self.__x1label, 1, 0)
        self.__layout.addWidget(self.x1val, 1, 1)

        self.__layout.addWidget(self.__y1label, 1, 2)
        self.__layout.addWidget(self.y1val, 1, 3)

        self.__layout.addWidget(self.__btn_ok, 2, 2)
        self.__layout.addWidget(self.__btn_cancel, 2, 3)

        self.retranslate_ui(widget)

        self.__set_default_values()

        self.__connections()

    def __set_default_values(self):
        self.x0val.setMinimum(0.0)
        self.x0val.setMaximum(1e8)
        self.x0val.setSingleStep(1)
        self.x0val.setValue(0.0)

        self.y0val.setMinimum(0.0)
        self.y0val.setMaximum(1e8)
        self.y0val.setSingleStep(1)
        self.y0val.setValue(0.0)

        self.x1val.setMinimum(0.0)
        self.x1val.setMaximum(1e8)
        self.x1val.setSingleStep(1)
        self.x1val.setValue(100.0)

        self.y1val.setMinimum(0.0)
        self.y1val.setMaximum(1e8)
        self.y1val.setSingleStep(1)
        self.y1val.setValue(25.0)

    def __connections(self):
        pass
        # self.__btn_ok.clicked.connect(self.accept)
        # self.__btn_cancel.clicked.connect(self.reject)
