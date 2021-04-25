from PyQt5 import QtCore

class Destination_Label():

    def __init__(self, destination_label) -> None:

        self.destination_label = destination_label
    
    def set_destination_label_style(self) -> None:
        self.destination_label.setGeometry(QtCore.QRect(20, 120, 81, 24))
        self.destination_label.setObjectName("destination_label")
        self.destination_label.setText("Destino:")

        return self.destination_label