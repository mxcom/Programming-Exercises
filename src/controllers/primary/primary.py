from datetime import datetime
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCore

from src.views.primary.WndMain import Ui_MainWindow


class PrimaryWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(PrimaryWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)