from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide6 import QtCore

from src.controllers.primary.progress_bar import CircularProgress
from src.controllers.user_management.calc_kcal import calc_kcal
from src.views.primary.WndMain import Ui_WndMain
from src.views.primary.uiFunctions import UIFunctions
from src.controllers.user_management.user_management import add_steps, add_weight, add_bp


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

        # Set Menu Button interaction
        # 0 Home Page
        # 1 Food Page
        # 2 Statistics Page Kcal
        # 3 Statistics Page Steps
        # 4 Statistics Page Blood Pressure
        # 5 Settings Page
        # 6 Admin Page
        self.ui.pages.setCurrentIndex(0)
        self.ui.btnHome.setStyleSheet(Style.style_btn_clicked_home)

        self.ui.btnHome.clicked.connect(self.home_page())
        self.ui.btnFood.clicked.connect(self.food_page())
        self.ui.btnStatistic.clicked.connect(self.stat_page())
        self.ui.btnSettings.clicked.connect(self.settings_page())

        # Functions for Button clicked

    def home_page(self):
        self.ui.pages.setCurrentIndex(0)
        self.ui.btnHome.setStyleSheet(Style.style_btn_clicked_home)
        self.ui.lbPageDescription.setText("Home")

    def food_page(self):
        self.ui.pages.setCurrentIndex(1)
        self.ui.btnFood.setStyleSheet(Style.style_btn_clicked_food)
        self.ui.lbPageDescription.setText("Food")

    def stat_page(self):
        self.ui.pages.setCurrentIndex(2)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_clicked_statistic)
        self.ui.lbPageDescription.setText("Statistics - Kcal")

    def settings_page(self):
        self.ui.pages.setCurrentIndex(5)
        self.ui.pageSettings.setStyleSheet(Style.style_btn_clicked_settings)
        self.ui.lbPageDescription.setText("Settings")

        # Test data
        # bd = datetime(2001, 1, 27)
        # self.progress = CircularProgress(calc_kcal("male", 196, 80, bd))

        self.progress.setMinimumSize(self.progress.width, self.progress.height)

        # Add widgets
        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)

        self.ui.btnToggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))

        self.ui.btnSubmit.clicked.connect(self.set_value)

        self.ui.leSteps.textChanged.connect(self.validate_steps)

        self.ui.leWeight.textChanged.connect(self.validate_weight)

        self.ui.leBPLow.textChanged.connect(self.validate_bp_low)
        self.ui.leBPHigh.textChanged.connect(self.validate_bp_high)

        # Set layout of the Frame
        self.ui.frmProgressBar.setLayout(self.layout)

    def validate_weight(self):
        try:
            input = int(self.ui.leWeight.text())
            self.ui.leWeight.setStyleSheet("color: black")
            return True
        except:
            self.ui.leWeight.setStyleSheet("color: rgb(255, 0, 65);")
            return False

    def validate_steps(self):
        try:
            input = int(self.ui.leSteps.text())
            self.ui.leSteps.setStyleSheet("color: black")
            return True
        except:
            self.ui.leSteps.setStyleSheet("color: rgb(255, 0, 65);")
            return False

    def validate_bp_low(self):
        try:
            input = int(self.ui.leBPLow.text())
            self.ui.leBPLow.setStyleSheet("color: Black")
            return True
        except:
            self.ui.leBPLow.setStyleSheet("color: rgb(255, 0, 65);")
            return False

    def validate_bp_high(self):
        try:
            text = int(self.ui.leBPLow.text())
            self.ui.leBPHigh.setStyleSheet("color: Black")
            return True
        except:
            self.ui.leBPHigh.setStyleSheet("color: rgb(255, 0, 65);")
            return False

    def set_value(self):
        if self.validate_steps():
            add_steps(self.user.get_id(), int(self.ui.leSteps.text()))

        if self.validate_steps():
            add_weight(self.user.get_id(), int(self.ui.leWeight.text()))

        if self.validate_bp_low() and self.validate_bp_high():
            add_bp(self.user.get_id(), int(self.ui.leBPLow.text()), int(self.ui.leBPHigh.text()))
