from PyQt5 import QtCore, QtGui

class Title_Label():

    def __init__(self, title_label) -> None:
        self.title_label = title_label
    
    def set_title_label_style(self) -> None:
        self.title_label.setGeometry(QtCore.QRect(100, 10, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("border-color: rgb(85, 87, 83);")
        self.title_label.setObjectName("title_label")
        self.title_label.setText("Organizador de arquivos por tipo")

        return self.title_label