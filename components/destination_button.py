from PyQt5.QtWidgets import QToolButton, QFileDialog


def Destination_Button(centralwidget, destination_path):

    def handle_destination_button():
        destination_path.setText("")
        directory = QFileDialog.getExistingDirectory(
            None, 'Selecione a pasta:', '/', QFileDialog.ShowDirsOnly)

        destination_path.setText(directory)

    destination_button = centralwidget.destination_button = QToolButton(centralwidget)
    destination_button.setGeometry(410, 120, 26, 24)
    destination_button.setObjectName("destination_button")
    destination_button.setText("...")

    destination_button.clicked.connect(handle_destination_button)

    return destination_button