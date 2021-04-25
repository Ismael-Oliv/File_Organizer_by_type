from PyQt5 import QtWidgets

def Status_Label(centralwidget):

    status_label = centralwidget.status_label = QtWidgets.QLabel(centralwidget)
    status_label.setGeometry(10, 270, 441, 23)
    status_label.setObjectName("status_label")
    status_label.setText("")

    return status_label