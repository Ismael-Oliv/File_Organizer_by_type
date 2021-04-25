from PyQt5 import QtCore

class Origin_Label():

    def __init__(self, origin_label) -> None:
        self.origin_label = origin_label
    
    def set_origin_label_style(self) -> None:
        self.origin_label.setGeometry(QtCore.QRect(20, 80, 81, 24))
        self.origin_label.setObjectName("origin_label")
        self.origin_label.setText("Origem :")

        return self.origin_label

    def get_text_value(self):
        return self.origin_label.text()