from datetime import datetime
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCore

from src.views.primary.WndMain import Ui_WndMain


class PrimaryWindow(QMainWindow, Ui_WndMain):

    def __init__(self, user, parent=None,):
        super(PrimaryWindow, self).__init__(parent)
        self.ui = Ui_WndMain()
        self.ui.setupUi(self)
        self.user = user

        self.ui.btnToggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))