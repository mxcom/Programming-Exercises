from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide6 import QtCore

from src.controllers.primary.progress_bar import CircularProgress
from src.controllers.user_management.calc_kcal import calc_kcal
from src.views.primary.WndMain import Ui_WndMain
from src.views.primary.uiFunctions import UIFunctions


class PrimaryWindow(QMainWindow, Ui_WndMain):

    def __init__(self, user, parent=None):
        super(PrimaryWindow, self).__init__(parent)
        self.ui = Ui_WndMain()
        self.ui.setupUi(self)
        self.user = user

        # Fill top Bar
        current_date = datetime.now()
        self.ui.lbName.setText(user.get_first_name() + " " + user.get_last_name())
        self.ui.lbDate.setText(current_date.strftime("%d.%m.%Y"))

        # Create Layout
        self.layout = QVBoxLayout()

        # Create porgress bar
        self.progress = CircularProgress(calc_kcal(
            user.get_sex(), user.get_height(), user.get_weight(), user.get_birthday()))

        # Test data
        # bd = datetime(2001, 1, 27)
        # self.progress = CircularProgress(calc_kcal("male", 196, 80, bd))

        self.progress.setMinimumSize(self.progress.width, self.progress.height)

        # Add widgets
        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)

        self.ui.btnToggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))

        # Set layout of the Frame
        self.ui.frmProgressBar.setLayout(self.layout)

        # Set Menu Button interaction
        # 0 Home Page
        # 1 Food Page
        # 2 Statistics Page
        # 3 Settings Page
        # 4 Admin Page

