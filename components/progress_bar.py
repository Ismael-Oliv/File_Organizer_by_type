from PyQt5.QtWidgets import QProgressBar

def Progress_Bar(centralwidget):

    progressBar = centralwidget.progressBar = QProgressBar(centralwidget)
    progressBar.setGeometry(10, 300, 441, 23)
    progressBar.setObjectName("progressBar")
    progressBar.setProperty("value", 0)

    return progressBar