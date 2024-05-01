import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.showMaximized()

app = QApplication(sys.argv)
QApplication.setApplicationName('THE RT BROWSER')
Window=MainWindow
app.exec_()
