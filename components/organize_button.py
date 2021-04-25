from PyQt5.QtWidgets import QToolButton
from services.organize_services import Organize_Services


def Organize_Button(centralwidget, origin_path, destination_path, progress_bar, status_label):

    def handle_organize_button():
        organize = Organize_Services(source=origin_path, destination_path=destination_path)
        organize.organize_file_by_type(progress_bar, status_label)


    organize_button = centralwidget.organize_button = QToolButton(centralwidget)
    organize_button.setGeometry(150, 170, 201, 51)
    organize_button.setObjectName("organize_button")
    organize_button.setText("Organizar")

    organize_button.clicked.connect(handle_organize_button)

    return organize_button