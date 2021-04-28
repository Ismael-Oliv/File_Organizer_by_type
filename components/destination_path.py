
from PyQt5 import QtWidgets


def Destination_Path(centralwidget):

    destination_path = centralwidget.destination_path = QtWidgets.QLabel(
        centralwidget)
    destination_path.setGeometry(100, 120, 291, 24)
    destination_path.setStyleSheet("""
                                    background-color: rgb(186, 189, 182);
                                    color: black;
                                """)
    # destination_path.setStyleSheet("color: black;")
    destination_path.setObjectName("destination_path")
    destination_path.setText("")

    return destination_path
