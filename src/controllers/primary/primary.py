from datetime import datetime
import re

from PySide6.QtCharts import QLineSeries, QChartView, QChart
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout
from PySide6 import QtCore
from PySide6.examples.charts.dynamicspline import chart

# from src.controllers.primary.stat_charts import create_chart
from src.controllers.user_management.user_management import update_email, update_passwd, update_height
from src.controllers.user_management.calorie_management import get_daily_calories, update_calories
from src.controllers.primary.progress_bar import CircularProgress
from src.controllers.user_management.calc_kcal import calc_kcal
from src.views.primary.WndMain import Ui_WndMain
from src.views.primary.btn_style import Style
from src.views.primary.uiFunctions import UIFunctions
from src.controllers.primary.stat_charts import Chart
from src.controllers.user_management.user_management import add_steps, add_weight, add_bp
from src.controllers.cryptography.cryptography import hash_passwd

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
special_char = ['$', '@', '#', '%', '_', '-', '!']


class PrimaryWindow(QMainWindow, Ui_WndMain):

    def __init__(self, user, parent=None):
        super(PrimaryWindow, self).__init__(parent)
        self.chart3 = None
        self.chart2 = None
        self.ui = Ui_WndMain()
        self.ui.setupUi(self)
        self.user = user

        self.ui.pages.setCurrentIndex(0)
        self.ui.frmLeftContentKcal.setMinimumSize(466, 470)

        kcal = get_daily_calories(user)

        # Fill top Bar
        current_date = datetime.now()
        self.ui.lbName.setText(user.get_first_name() + " " + user.get_last_name())
        self.ui.lbDate.setText(current_date.strftime("%d.%m.%Y"))

        # Create Layout
        self.layout = QVBoxLayout()

        # Create porgress bar
        self.progress = CircularProgress(0, kcal, calc_kcal(
            self.user.get_sex(), self.user.get_height(), self.user.get_weight(), self.user.get_birthday()))

        # Test data
        # bd = datetime(2001, 1, 27)
        # self.progress = CircularProgress(calc_kcal("male", 196, 80, bd))

        self.progress.setMinimumSize(self.progress.width, self.progress.height)

        # Add widgets
        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)

        # Set layout of the Frame
        self.ui.frmProgressBar.setLayout(self.layout)

        # Set Menu Button interaction
        # 0 Home Page
        # 1 Food Page
        # 2 Statistics Page Kcal
        # 3 Statistics Page Steps
        # 4 Statistics Page Blood Pressure
        # 5 Settings Page
        # 6 Admin Page

        self.ui.btnHome.setStyleSheet(Style.style_btn_selected_home)

        self.ui.btnHome.clicked.connect(self.home_page)
        self.ui.btnFood.clicked.connect(self.food_page)
        self.ui.btnStatistic.clicked.connect(self.stat_page_kcal)
        self.ui.btnSettings.clicked.connect(self.settings_page)
        self.ui.btnKcal1.clicked.connect(self.stat_page_kcal)
        self.ui.btnKcal2.clicked.connect(self.stat_page_kcal)
        self.ui.btnKcal3.clicked.connect(self.stat_page_kcal)
        self.ui.btnSteps1.clicked.connect(self.stat_page_steps)
        self.ui.btnSteps2.clicked.connect(self.stat_page_steps)
        self.ui.btnSteps3.clicked.connect(self.stat_page_steps)
        self.ui.btnBP1.clicked.connect(self.stat_page_bp)
        self.ui.btnBP2.clicked.connect(self.stat_page_bp)
        self.ui.btnBP3.clicked.connect(self.stat_page_bp)
        self.ui.btnToggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))

        # Tracking interface button / line edit interaction
        self.ui.btnSubmit.clicked.connect(self.set_value)

        self.ui.leSteps.textChanged.connect(self.validate_steps)

        self.ui.leWeight.textChanged.connect(self.validate_weight)

        self.ui.leBPLow.textChanged.connect(self.validate_bp_low)
        self.ui.leBPHigh.textChanged.connect(self.validate_bp_high)

        self.ui.cbKcal.activated.connect(self.date_selected)

        # Set statistics
        self.chart = Chart(self.user, 1)
        self.kcal_chart = self.chart.get_chartview()
        # self.chart = create_chart(self.user, 1)
        self.layoutChart = QHBoxLayout()
        self.layoutChart.addWidget(self.kcal_chart)
        self.ui.kcalChart.setLayout(self.layoutChart)
        self.ui.lbAvgKcalValue.setText(self.chart.get_avg_value())
        self.ui.lbMaxKcalValue.setText(self.chart.get_max_value())
        self.ui.lbMinKcalValue.setText(self.chart.get_min_value())


        # Set Setting page Functionalities
        self.ui.lbSetFirstNameValue.setText(self.user.get_first_name())
        self.ui.lbSetFirstNameValue.setStyleSheet("color: rgb(211, 201, 242);")
        self.ui.lbSetLastNameValue.setText(self.user.get_last_name())
        self.ui.lbSetLastNameValue.setStyleSheet("color: rgb(211, 201, 242);")
        self.ui.lbSetBirthdayValue.setText(self.user.get_birthday().strftime("%d.%m.%Y"))
        self.ui.lbSetBirthdayValue.setStyleSheet("color: rgb(211, 201, 242);")
        self.ui.lbSetSexValue.setText(self.user.get_sex())
        self.ui.lbSetSexValue.setStyleSheet("color: rgb(211, 201, 242);")
        self.ui.lbSetHeightValue.setText((str(int(self.user.get_height()))) + " cm")
        self.ui.lbSetHeightValue.setStyleSheet("color: rgb(211, 201, 242);")
        self.ui.lbSetEmailValue.setText(self.user.get_email())
        self.ui.lbSetEmailValue.setStyleSheet("color: rgb(211, 201, 242);")

        self.ui.btnChangeInfo.clicked.connect(self.change_infos)

    # Methods for Menu Button clicked
    def home_page(self):
        self.ui.pages.setCurrentIndex(0)
        self.ui.btnHome.setStyleSheet(Style.style_btn_selected_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_default_statistic)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.lbPageDescription.setText("Home")

    def food_page(self):
        self.ui.pages.setCurrentIndex(1)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_selected_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_default_statistic)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.lbPageDescription.setText("Food")

    def stat_page_kcal(self):
        self.ui.pages.setCurrentIndex(2)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_selected_statistic)
        self.ui.btnKcal1.setStyleSheet(Style.style_btn_selected_stat_controle)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.lbPageDescription.setText("Statistics - Kcal")

    def stat_page_steps(self):
        self.ui.pages.setCurrentIndex(3)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_selected_statistic)
        self.ui.btnSteps2.setStyleSheet(Style.style_btn_selected_stat_controle)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.lbPageDescription.setText("Statistics - Steps")

    def stat_page_bp(self):
        self.ui.pages.setCurrentIndex(4)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_selected_statistic)
        self.ui.btnBP3.setStyleSheet(Style.style_btn_selected_stat_controle)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.lbPageDescription.setText("Statistics - Blood Pressure")

    def settings_page(self):
        self.ui.pages.setCurrentIndex(5)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_default_statistic)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_selected_settings)
        self.ui.lbPageDescription.setText("Settings")

    # Methods to validate the entered tracking data
    def validate_weight(self):
        try:
            input = int(self.ui.leWeight.text())
            self.ui.leWeight.setStyleSheet("color: black")
            if input < 0:
                self.ui.leWeight.setStyleSheet("color: rgb(255, 0, 65);")
                return False
            else:
                return False
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
            return True
        except:
            return False

    def validate_bp_high(self):
        try:
            text = int(self.ui.leBPLow.text())
            return True
        except:
            return False

    def add_calories(self, old_calories, new_calories):
        self.progress.hide()
        self.progress = CircularProgress(old_calories, new_calories,
                                         calc_kcal(self.user.get_sex(), self.user.get_height(), self.user.get_weight(),
                                                   self.user.get_birthday()))
        self.progress.setMinimumSize(self.progress.width, self.progress.height)

        # Add widgets
        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)

        # Set layout of the Frame
        self.ui.frmProgressBar.setLayout(self.layout)

    def set_value(self):
        old_calories = get_daily_calories(self.user)
        new_calories = update_calories(self.user, old_calories, 250)
        self.add_calories(old_calories, new_calories)

        # if self.validate_steps():
        #     add_steps(self.user.get_id(), int(self.ui.leSteps.text()))

        # if self.validate_steps():
        #     add_weight(self.user.get_id(), int(self.ui.leWeight.text()))

        # if self.validate_bp_low() and self.validate_bp_high():
        #     add_bp(self.user.get_id(), int(self.ui.leBPLow.text()), int(self.ui.leBPHigh.text()))

    def date_selected(self):
        if self.ui.cbKcal.currentText() == '1 week':
            self.chart = Chart(self.user, 1)
            self.layoutChart.removeWidget(self.kcal_chart)
            self.kcal_chart = self.chart.get_chartview()
            self.layoutChart.addWidget(self.kcal_chart)
            self.ui.kcalChart.setLayout(self.layoutChart)
            self.ui.lbAvgKcalValue.setText(self.chart.get_avg_value())
            self.ui.lbMaxKcalValue.setText(self.chart.get_max_value())
            self.ui.lbMinKcalValue.setText(self.chart.get_min_value())
        if self.ui.cbKcal.currentText() == '1 month':
            chart2 = Chart(self.user, 2)
            self.layoutChart.removeWidget(self.kcal_chart)
            self.kcal_chart = chart2.get_chartview()
            self.layoutChart.addWidget(self.kcal_chart)
            self.ui.kcalChart.setLayout(self.layoutChart)
            self.ui.lbAvgKcalValue.setText(chart2.get_avg_value())
            self.ui.lbMaxKcalValue.setText(chart2.get_max_value())
            self.ui.lbMinKcalValue.setText(chart2.get_min_value())

        if self.ui.cbKcal.currentText() == 'complete':
            chart3 = Chart(self.user, 3)
            self.layoutChart.removeWidget(self.kcal_chart)
            self.kcal_chart = chart3.get_chartview()
            self.layoutChart.addWidget(self.kcal_chart)
            self.ui.kcalChart.setLayout(self.layoutChart)
            self.ui.lbAvgKcalValue.setText(chart3.get_avg_value())
            self.ui.lbMaxKcalValue.setText(chart3.get_max_value())
            self.ui.lbMinKcalValue.setText(chart3.get_min_value())

    def validate_email(self):
        try:
            email = self.ui.leSetEmail.text()
            if re.fullmatch(regex, email):
                if self.ui.leSetEmail.text() == self.ui.leSetConfirmEmail.text():
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def validate_passwd(self):
        try:
            passwd = self.ui.leSetPassword.text()
            if not any(char.isupper() for char in passwd):
                return False

            # Password needs to contain at least 1 lowercase letter
            if not any(char.islower() for char in passwd):
                return False

            # Password needs to contain at least 1 digit
            if not any(char.isdigit() for char in passwd):
                return False

            # Password needs to contain at least 1 special character
            if not any(char in special_char for char in passwd):
                return False

            # Password needs to be >= 8 characters
            if len(passwd) < 8:
                return False

            if passwd == self.ui.leSetConfirmPassword.text():
                return True
        except Exception as e:
            print(e)
            return False

    def validate_height(self):
        try:
            input_int = int(self.ui.leSetHeight.text())
            if 140 < input_int < 250:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def change_infos(self):
        if self.validate_email():
            if update_email(self.user, self.ui.leSetEmail.text()):
                self.user.set_email(self.ui.leSetEmail.text())
                self.ui.lbSetEmailValue.setText(self.ui.leSetEmail.text())
                self.ui.leSetEmail.setText('')
                self.ui.leSetConfirmEmail.setText('')
            else:
                self.lbSetError.setText("Email could not be updated")

        if self.validate_passwd():
            if update_passwd(self.user, self.ui.leSetPassword.text()):
                self.ui.leSetPassword.setText('')
                self.ui.leSetConfirmPassword.setText('')
            else:
                self.lbSetError.setText("Password could not be updated")

        if self.validate_height():
            if update_height(self.user, self.ui.leSetHeight.text()):
                self.user.set_height(self.ui.leSetHeight.text())
                self.ui.lbSetHeightValue.setText(self.ui.leSetHeight.text())
                self.ui.leSetHeight.setText('')
            else:
                self.lbSetError.setText("Height could not be updated")
