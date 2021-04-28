from PyQt5 import QtCore, QtWidgets


def Origin_Path(centralwidget):

    origin_path = centralwidget.origin_path = QtWidgets.QLabel(centralwidget)
    origin_path.setGeometry(100, 76, 291, 24)
    origin_path.setStyleSheet("""background-color: rgb(186, 189, 182);
                                color: black;
                                """)
    # origin_path.setStyleSheet("font: black;")
    origin_path.setObjectName("origin_path")
    origin_path.setText("")

    return origin_path
