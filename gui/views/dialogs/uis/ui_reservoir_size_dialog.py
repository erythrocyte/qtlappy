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

        self.__x0val = QtWidgets.QDoubleSpinBox(self)
        self.__y0val = QtWidgets.QDoubleSpinBox(self)
        self.__x1val = QtWidgets.QDoubleSpinBox(self)
        self.__y1val = QtWidgets.QDoubleSpinBox(self)

        self.__layout = QtWidgets.QGridLayout(self)

    def retranslate_ui(self):
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

    def setup_ui(self, widget: QtWidgets.QWidget):
        """
        """
        widget.setLayout(self.__layout)

        self.__layout.addWidget(self.__x0label, 0, 0)
        self.__layout.addWidget(self.__x0val, 0, 1)

        self.__layout.addWidget(self.__y0label, 0, 2)
        self.__layout.addWidget(self.__y0val, 0, 3)

        self.__layout.addWidget(self.__x1label, 1, 0)
        self.__layout.addWidget(self.__x1val, 1, 1)

        self.__layout.addWidget(self.__y1label, 1, 2)
        self.__layout.addWidget(self.__y1val, 1, 3)

        self.retranslate_ui()

        self.__set_default_values()

    def __set_default_values(self):
        self.__x0val.setValue(0.0)
        self.__y0val.setValue(0.0)
        self.__x1val.setValue(100.0)
        self.__y1val.setValue(25.0)
