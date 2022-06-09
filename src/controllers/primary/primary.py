from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide6 import QtCore

from src.controllers.primary.progress_bar import CircularProgress
from src.controllers.user_management.calc_kcal import calc_kcal
from src.views.primary.WndMain import Ui_WndMain
from src.views.primary.uiFunctions import UIFunctions


class PrimaryWindow(QMainWindow, Ui_WndMain):

    def __init__(self, user, parent=None,):
        super(PrimaryWindow, self).__init__(parent)
        self.ui = Ui_WndMain()
        self.ui.setupUi(self)
        self.user = user

        # Create Layout
        self.layout = QVBoxLayout()

        # Create porgress bar
        self.progress = CircularProgress(calc_kcal(
            user.get_sex(), user.get_height(), user.get_weight(), user.get_birthday()))

        self.progress.setMinimumSize(self.progress.width, self.progress.height)

        # Add widgets
        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)

        self.ui.btnToggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))

        # Set layout of the Frame
        self.frmProgressBar.setLayout(self.layout)
