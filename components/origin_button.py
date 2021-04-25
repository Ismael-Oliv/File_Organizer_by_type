from PyQt5.QtWidgets import QToolButton, QFileDialog


def Origin_Button(centralwidget, origin_path):

    def handle_origin_button():
        origin_path.setText("")
        directory = QFileDialog.getExistingDirectory(
            None, 'Selecione a pasta:', '/', QFileDialog.ShowDirsOnly)

        origin_path.setText(directory)

    origin_button = centralwidget.origin_button = QToolButton(centralwidget)
    origin_button.setGeometry(410, 76, 26, 24)
    origin_button.setObjectName("origin_button")
    origin_button.setText("...")

    origin_button.clicked.connect(handle_origin_button)

    return origin_button