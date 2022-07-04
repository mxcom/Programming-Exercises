from datetime import datetime
import re, json

from PySide6.QtCharts import QLineSeries, QChartView, QChart
from PySide6.QtCore import Qt, QPointF, QTimer, QDate
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout , QTableWidgetItem
from PySide6 import QtCore
from PySide6.examples.charts.dynamicspline import chart

# from src.controllers.primary.stat_charts import create_chart
from src.controllers.primary.stat_charts_kcal import ChartKcal
from src.controllers.primary.stat_charts_steps import ChartSteps
from src.controllers.primary.stat_charts_bp import ChartBp
from src.controllers.primary.stat_charts_weight import ChartWeight
from src.controllers.user_management.user_management import update_email, update_passwd, update_height
from src.controllers.user_management.calorie_management import get_daily_calories, update_calories, get_food_from_date
from src.controllers.primary.progress_bar import CircularProgress
from src.controllers.user_management.calc_kcal import calc_kcal
from src.views.primary.WndMain import Ui_WndMain
from src.views.primary.btn_style import Style
from src.views.primary.uiFunctions import UIFunctions
from src.controllers.primary import *
from src.controllers.user_management.user_management import add_steps, add_weight, add_bp
from src.controllers.cryptography.cryptography import hash_passwd
from src.controllers.open_food_facts import open_food_facts

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
special_char = ['$', '@', '#', '%', '_', '-', '!']


class PrimaryWindow(QMainWindow, Ui_WndMain):

    def __init__(self, user, LoginWindow, parent=None):
        super(PrimaryWindow, self).__init__(parent)
        self.ui = Ui_WndMain()
        self.ui.setupUi(self)
        self.user = user

        self.LoginWindow = LoginWindow
        self.ui.pages.setCurrentIndex(0)
        self.ui.frmLeftContentKcal.setMinimumSize(466, 470)

        kcal = get_daily_calories(user)

        # Fill top Bar
        current_date = datetime.now()
        self.ui.lbName.setText(str(user.get_first_name()) + " " + str(user.get_last_name()))
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

        self.ui.label_3.hide()

        self.ui.btnHome.clicked.connect(self.home_page)
        self.ui.btnFood.clicked.connect(self.food_page)
        self.ui.btnStatistic.clicked.connect(self.stat_page_kcal)
        self.ui.btnSettings.clicked.connect(self.settings_page)
        self.ui.btnCalendar.clicked.connect(self.calendar_page)
        self.ui.btnLogout.clicked.connect(self.logout)
        self.ui.btnKcal1.clicked.connect(self.stat_page_kcal)
        self.ui.btnKcal2.clicked.connect(self.stat_page_kcal)
        self.ui.btnKcal3.clicked.connect(self.stat_page_kcal)
        self.ui.btnKcal4.clicked.connect(self.stat_page_kcal)
        self.ui.btnSteps1.clicked.connect(self.stat_page_steps)
        self.ui.btnSteps2.clicked.connect(self.stat_page_steps)
        self.ui.btnSteps3.clicked.connect(self.stat_page_steps)
        self.ui.btnSteps4.clicked.connect(self.stat_page_steps)
        self.ui.btnBP1.clicked.connect(self.stat_page_bp)
        self.ui.btnBP2.clicked.connect(self.stat_page_bp)
        self.ui.btnBP3.clicked.connect(self.stat_page_bp)
        self.ui.btnBP4.clicked.connect(self.stat_page_bp)
        self.ui.btnWeight1.clicked.connect(self.stat_page_weight)
        self.ui.btnWeight2.clicked.connect(self.stat_page_weight)
        self.ui.btnWeight3.clicked.connect(self.stat_page_weight)
        self.ui.btnWeight4.clicked.connect(self.stat_page_weight)
        self.ui.btnToggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))
        # Tracking interface button / line edit interaction
        self.ui.btnSubmit.clicked.connect(self.set_value)

        self.ui.leSteps.textChanged.connect(self.validate_steps)

        self.ui.leWeight.textChanged.connect(self.validate_weight)

        self.ui.leBPLow.textChanged.connect(self.validate_bp_low)
        self.ui.leBPHigh.textChanged.connect(self.validate_bp_high)

        # Connect Combooxes for Chart selcetion to methods
        self.ui.cbKcal.activated.connect(self.date_selected_kcal)
        self.ui.cbSteps.activated.connect(self.date_selected_steps)
        self.ui.cbBP.activated.connect(self.date_selected_bp)
        self.ui.cbWeight.activated.connect(self.date_selected_weight)

        # Set statistics
        self.chart_kcal_1 = ChartKcal(self.user, 1)
        self.kcal_chart = self.chart_kcal_1.get_chartview()
        self.layout_chart_kcal = QHBoxLayout()
        self.layout_chart_kcal.addWidget(self.kcal_chart)
        self.ui.kcalChart.setLayout(self.layout_chart_kcal)
        self.ui.lbAvgKcalValue.setText(self.chart_kcal_1.get_avg_value())
        self.ui.lbMaxKcalValue.setText(self.chart_kcal_1.get_max_value())
        self.ui.lbMinKcalValue.setText(self.chart_kcal_1.get_min_value())
        # self.chart_kcal_3 = ChartKcal(self.user, 3)
        self.kcal_chart_3 = self.chart_kcal_1.get_chartview()
        self.kcal_chart_2 = self.chart_kcal_1.get_chartview()

        self.chart_steps_1 = ChartSteps(self.user, 1)
        self.steps_chart = self.chart_steps_1.get_chartview()
        self.layout_chart_steps = QHBoxLayout()
        self.layout_chart_steps.addWidget(self.steps_chart)
        self.ui.stepsChart.setLayout(self.layout_chart_steps)
        self.ui.lbAvgStepsValue.setText(str(self.chart_steps_1.get_avg_value()))
        self.ui.lbMaxStepsValue.setText(str(self.chart_steps_1.get_max_value()))
        self.ui.lbMinStepsValue.setText(str(self.chart_steps_1.get_min_value()))
        self.chart_steps_2 = ChartSteps(self.user, 2)
        self.chart_steps_3 = ChartSteps(self.user, 3)
        self.steps_chart_2 = self.chart_steps_1.get_chartview()
        self.steps_chart_3 = self.chart_steps_1.get_chartview()

        self.chart_bp_1 = ChartBp(self.user, 1)
        self.bp_chart = self.chart_bp_1.get_chartview()
        self.layout_chart_bp = QHBoxLayout()
        self.layout_chart_bp.addWidget(self.bp_chart)
        self.ui.bpChart.setLayout(self.layout_chart_bp)
        self.ui.lbAvgBpValue.setText(self.chart_bp_1.get_avg_value())
        self.ui.lbMaxBpValue.setText(self.chart_bp_1.get_max_value())
        self.ui.lbMinBpValue.setText(self.chart_bp_1.get_min_value())
        # self.chart_bp_3 = ChartBp(self.user, 3)
        self.bp_chart_2 = self.chart_bp_1.get_chartview()
        self.bp_chart_3 = self.chart_bp_1.get_chartview()

        self.chart_weight_1 = ChartWeight(self.user, 1)
        self.weight_chart = self.chart_weight_1.get_chartview()
        self.layout_chart_weight = QHBoxLayout()
        self.layout_chart_weight.addWidget(self.weight_chart)
        self.ui.weightChart.setLayout(self.layout_chart_weight)
        self.ui.lbAvgWeightValue.setText(self.chart_weight_1.get_avg_value())
        self.ui.lbMaxWeightValue.setText(self.chart_weight_1.get_max_value())
        self.ui.lbMinWeightValue.setText(self.chart_weight_1.get_min_value())
        self.weight_chart_2 = self.chart_weight_1.get_chartview()
        self.weight_chart_3 = self.chart_weight_1.get_chartview()

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
        # OpenFoodfacts
        self.ui.btnSearchFood.clicked.connect(self.search_name)
        self.ui.tbFood.cellClicked.connect(self.table_click)
        self.ui.btnAddFood.clicked.connect(self.add_food)

        self.ui.calendarWidget.clicked[QtCore.QDate].connect(self.calendar_click)

    def calendar_click(self):
        date = self.ui.calendarWidget.selectedDate().toPython()
        if date > datetime.today().date():
            self.ui.calendarWidget.setSelectedDate(QDate.currentDate())
            track = get_food_from_date(datetime.today().date(), self.user)
            self.ui.lbCalendarKcal.setText(str(track.get_calories_eaten()))
            self.ui.lbCalendarSteps.setText(str(track.get_steps_walked()))
            self.ui.lbCalendarWeight.setText(str(track.get_weight()))
            self.ui.lbCalendarBP.setText(str(track.get_bloodpressure()))
        else:
            track = get_food_from_date(self.ui.calendarWidget.selectedDate().toPython(), self.user)
            self.ui.lbCalendarKcal.setText(str(track.get_calories_eaten()))
            self.ui.lbCalendarKcal.setStyleSheet(u"color: rgb(211, 201, 242);")
            self.ui.lbCalendarSteps.setText(str(track.get_steps_walked()))
            self.ui.lbCalendarSteps.setStyleSheet(u"color: rgb(211, 201, 242);")
            self.ui.lbCalendarWeight.setText(str(track.get_weight()))
            self.ui.lbCalendarWeight.setStyleSheet(u"color: rgb(211, 201, 242);")
            self.ui.lbCalendarBP.setText(str(track.get_bloodpressure()))
            self.ui.lbCalendarBP.setStyleSheet(u"color: rgb(211, 201, 242);")

    def table_click(self,row,column):
        item=self.ui.tbFood.item(row,1)
        self.ui.leCalories.setText(item.text())

    def add_food(self):
        # daily calories
        old_calories = get_daily_calories(self.user)

        # calories from textfield
        calories = self.ui.leCalories.text()

        # how many times calories
        amount = self.ui.leAmount.text()

        # calculate new calories
        new_calories = (float(calories)/100)*float(amount)

        # update calories in database
        update_calories(self.user, old_calories, new_calories)

        self.add_calories(old_calories, int(new_calories+old_calories))

    def search_name(self):
        results = open_food_facts.search_name(self.ui.leSearchFood.text())
        self.ui.tbFood.clear()
        self.ui.tbFood.clearContents()
        self.ui.tbFood.setRowCount(0)
        i = 0
        for key in results["products"]:
            self.ui.tbFood.insertRow(i)
            if 'product_name_de' in key:
                if key['product_name_de'].isalnum() & len(key['product_name_de']) > 0:
                    self.ui.tbFood.setItem(i, 0,  QTableWidgetItem(key['product_name_de']))
                else:
                    self.ui.tbFood.setItem(i, 0,  QTableWidgetItem(key['product_name']))
            self.ui.tbFood.setItem(i, 1,  QTableWidgetItem(str(key['nutriments']['energy-kcal_100g'])))
            i = i + 1

        self.ui.tbFood.setHorizontalHeaderItem(0, QTableWidgetItem("Names"))
        self.ui.tbFood.setHorizontalHeaderItem(1, QTableWidgetItem("Calories per 100g"))
        self.ui.tbFood.resizeColumnsToContents()


    # Methods for Menu Button clicked
    def home_page(self):
        self.ui.pages.setCurrentIndex(0)
        self.ui.btnHome.setStyleSheet(Style.style_btn_selected_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_default_statistic)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.btnCalendar.setStyleSheet(Style.style_btn_default_calendar)
        self.ui.lbPageDescription.setText("Home")

    def food_page(self):
        self.ui.pages.setCurrentIndex(1)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_selected_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_default_statistic)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.btnCalendar.setStyleSheet(Style.style_btn_default_calendar)
        self.ui.lbPageDescription.setText("Food")

    def stat_page_kcal(self):
        self.ui.pages.setCurrentIndex(2)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_selected_statistic)
        self.ui.btnKcal1.setStyleSheet(Style.style_btn_selected_stat_controle)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.btnCalendar.setStyleSheet(Style.style_btn_default_calendar)
        self.ui.lbPageDescription.setText("Statistics - Kcal")

    def stat_page_steps(self):
        self.ui.pages.setCurrentIndex(3)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_selected_statistic)
        self.ui.btnSteps2.setStyleSheet(Style.style_btn_selected_stat_controle)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.btnCalendar.setStyleSheet(Style.style_btn_default_calendar)
        self.ui.lbPageDescription.setText("Statistics - Steps")

    def stat_page_bp(self):
        self.ui.pages.setCurrentIndex(4)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_selected_statistic)
        self.ui.btnBP3.setStyleSheet(Style.style_btn_selected_stat_controle)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.btnCalendar.setStyleSheet(Style.style_btn_default_calendar)
        self.ui.lbPageDescription.setText("Statistics - Blood Pressure")

    def stat_page_weight(self):
        self.ui.pages.setCurrentIndex(5)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_selected_statistic)
        self.ui.btnWeight4.setStyleSheet(Style.style_btn_selected_stat_controle)
        self.ui.btnCalendar.setStyleSheet(Style.style_btn_default_calendar)
        self.ui.lbPageDescription.setText("Statistics - Weight")

    def settings_page(self):
        self.ui.pages.setCurrentIndex(6)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_default_statistic)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_selected_settings)
        self.ui.btnCalendar.setStyleSheet(Style.style_btn_default_calendar)
        self.ui.lbPageDescription.setText("Settings")

    def calendar_page(self):
        self.ui.pages.setCurrentIndex(7)
        self.ui.btnHome.setStyleSheet(Style.style_btn_default_home)
        self.ui.btnFood.setStyleSheet(Style.style_btn_default_food)
        self.ui.btnStatistic.setStyleSheet(Style.style_btn_default_statistic)
        self.ui.btnSettings.setStyleSheet(Style.style_btn_default_settings)
        self.ui.btnCalendar.setStyleSheet(Style.style_btn_selected_calendar)
        self.ui.lbPageDescription.setText("Calendar")

    def logout(self):
        try:
            self.destroy()
            self.LoginWindow.show()
        except Exception as e:
            print(e)

    # Methods to validate the entered tracking data
    def validate_weight(self):
        try:
            input = float(self.ui.leWeight.text())
            self.ui.leWeight.setStyleSheet("color: black; border-bottom: 2px solid rgb(211, 201, 242);")
            if input < 0:
                return False
            else:
                return True
        except:
            self.ui.leWeight.setStyleSheet("color: black; border-bottom: 2px solid rgb(211, 201, 242);")
            return False

    def validate_steps(self):
        try:
            input = int(self.ui.leSteps.text())
            self.ui.leSteps.setStyleSheet("color: black; border-bottom: 2px solid rgb(211, 201, 242);")
            if input < 0:
                return False
            else:
                return True
        except:
            self.ui.leSteps.setStyleSheet("color: black; border-bottom: 2px solid rgb(211, 201, 242);")
            return False

    def validate_bp_low(self):
        try:
            input = int(self.ui.leBPLow.text())
            if input < 0:
                return False
            else:
                return True
        except:
            return False

    def validate_bp_high(self):
        try:
            input = int(self.ui.leBPLow.text())
            if input < 0:
                return False
            else:
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
        # old_calories = get_daily_calories(self.user)
        # new_calories = update_calories(self.user, old_calories, 250)
        # self.add_calories(old_calories, new_calories)

        if self.validate_weight():
            add_weight(self.user.get_id(), int(self.ui.leWeight.text()))

        if self.validate_steps():
            add_steps(self.user.get_id(), int(self.ui.leSteps.text()))

        if self.validate_bp_low() and self.validate_bp_high():
            add_bp(self.user.get_id(), int(self.ui.leBPLow.text()), int(self.ui.leBPHigh.text()))

        timer = QTimer()
        timer.singleShot(0, self.show_label)
        timer.singleShot(6000, self.hide_label)

    def show_label(self):
        self.ui.label_3.show()

    def hide_label(self):
        self.ui.label_3.hide()


    def date_selected_kcal(self):
        # kcla 1 week
        if self.ui.cbKcal.currentText() == '1 week':
            self.chart_kcal_1 = ChartKcal(self.user, 1)
            self.kcal_chart_2.hide()
            self.kcal_chart_3.hide()
            self.kcal_chart = self.chart_kcal_1.get_chartview()
            self.layout_chart_kcal.removeWidget(self.kcal_chart)
            self.layout_chart_kcal.addWidget(self.kcal_chart)
            self.ui.kcalChart.setLayout(self.layout_chart_kcal)
            self.ui.lbAvgKcalValue.setText(self.chart_kcal_1.get_avg_value())
            self.ui.lbMaxKcalValue.setText(self.chart_kcal_1.get_max_value())
            self.ui.lbMinKcalValue.setText(self.chart_kcal_1.get_min_value())
        # kcal 1 month
        if self.ui.cbKcal.currentText() == '1 month':
            self.chart_kcal_2 = ChartKcal(self.user, 2)
            self.kcal_chart_3.hide()
            self.kcal_chart.hide()
            self.kcal_chart_2 = self.chart_kcal_2.get_chartview()
            self.layout_chart_kcal.removeWidget(self.kcal_chart)
            self.layout_chart_kcal.addWidget(self.kcal_chart_2)
            self.ui.kcalChart.setLayout(self.layout_chart_kcal)
            self.ui.lbAvgKcalValue.setText(self.chart_kcal_2.get_avg_value())
            self.ui.lbMaxKcalValue.setText(self.chart_kcal_2.get_max_value())
            self.ui.lbMinKcalValue.setText(self.chart_kcal_2.get_min_value())
        # kcal complete
        if self.ui.cbKcal.currentText() == 'complete':
            self.chart_kcal_3 = ChartKcal(self.user, 3)
            self.kcal_chart_2.hide()
            self.kcal_chart.hide()
            self.kcal_chart_3 = self.chart_kcal_3.get_chartview()
            self.layout_chart_kcal.removeWidget(self.kcal_chart)
            self.layout_chart_kcal.addWidget(self.kcal_chart_3)
            self.ui.kcalChart.setLayout(self.layout_chart_kcal)
            self.ui.lbAvgKcalValue.setText(self.chart_kcal_3.get_avg_value())
            self.ui.lbMaxKcalValue.setText(self.chart_kcal_3.get_max_value())
            self.ui.lbMinKcalValue.setText(self.chart_kcal_3.get_min_value())

    def date_selected_steps(self):
        # steps 1 week
        if self.ui.cbSteps.currentText() == '1 week':
            self.chart_steps_1 = ChartSteps(self.user, 1)
            self.steps_chart_2.hide()
            self.steps_chart_3.hide()
            self.layout_chart_steps.removeWidget(self.steps_chart)
            self.steps_chart = self.chart_steps_1.get_chartview()
            self.layout_chart_steps.addWidget(self.steps_chart)
            self.ui.stepsChart.setLayout(self.layout_chart_steps)
            self.ui.lbAvgStepsValue.setText(self.chart_steps_1.get_avg_value())
            self.ui.lbMaxStepsValue.setText(self.chart_steps_1.get_max_value())
            self.ui.lbMinStepsValue.setText(self.chart_steps_1.get_min_value())

        # steps 1 month
        if self.ui.cbSteps.currentText() == '1 month':
            self.chart_steps_2 = ChartKcal(self.user, 2)
            self.steps_chart.hide()
            self.steps_chart_3.hide()
            self.layout_chart_steps.removeWidget(self.steps_chart)
            self.steps_chart_2 = self.chart_steps_2.get_chartview()
            self.layout_chart_steps.addWidget(self.steps_chart_2)
            self.ui.stepsChart.setLayout(self.layout_chart_steps)
            self.ui.lbAvgStepsValue.setText(self.chart_steps_2.get_avg_value())
            self.ui.lbMaxStepsValue.setText(self.chart_steps_2.get_max_value())
            self.ui.lbMinStepsValue.setText(self.chart_steps_2.get_min_value())

        # steps complete
        if self.ui.cbSteps.currentText() == 'complete':
            self.chart_steps_3 = ChartKcal(self.user, 3)
            self.steps_chart.hide()
            self.steps_chart_2.hide()
            self.layout_chart_steps.removeWidget(self.steps_chart)
            self.steps_chart_3 = self.chart_steps_3.get_chartview()
            self.layout_chart_steps.addWidget(self.steps_chart_3)
            self.ui.stepsChart.setLayout(self.layout_chart_steps)
            self.ui.lbAvgStepsValue.setText(self.chart_steps_3.get_avg_value())
            self.ui.lbMaxStepsValue.setText(self.chart_steps_3.get_max_value())
            self.ui.lbMinStepsValue.setText(self.chart_steps_3.get_min_value())

    def date_selected_bp(self):
        if self.ui.cbBP.currentText() == '1 week':
            self.chart_bp_1 = ChartBp(self.user, 1)
            self.bp_chart_2.hide()
            self.bp_chart_3.hide()
            self.bp_chart = self.chart_bp_1.get_chartview()
            self.layout_chart_bp.addWidget(self.bp_chart)
            self.ui.bpChart.setLayout(self.layout_chart_bp)
            self.ui.lbAvgBpValue.setText(self.chart_bp_1.get_avg_value())
            self.ui.lbMaxBpValue.setText(self.chart_bp_1.get_max_value())
            self.ui.lbMinBpValue.setText(self.chart_bp_1.get_min_value())

        if self.ui.cbBP.currentText() == '1 month':
            self.chart_bp_2 = ChartBp(self.user, 2)
            self.bp_chart.hide()
            self.bp_chart_3.hide()
            self.bp_chart_2 = self.chart_bp_2.get_chartview()
            self.layout_chart_bp.addWidget(self.bp_chart_2)
            self.ui.bpChart.setLayout(self.layout_chart_bp)
            self.ui.lbAvgBpValue.setText(self.chart_bp_2.get_avg_value())
            self.ui.lbMaxBpValue.setText(self.chart_bp_2.get_max_value())
            self.ui.lbMinBpValue.setText(self.chart_bp_2.get_min_value())

        if self.ui.cbBP.currentText() == 'complete':
            self.chart_bp_3 = ChartBp(self.user, 3)
            self.bp_chart.hide()
            self.bp_chart_2.hide()
            self.bp_chart_3 = self.chart_bp_3.get_chartview()
            self.layout_chart_bp.addWidget(self.bp_chart_3)
            self.ui.bpChart.setLayout(self.layout_chart_bp)
            self.ui.lbAvgBpValue.setText(self.chart_bp_3.get_avg_value())
            self.ui.lbMaxBpValue.setText(self.chart_bp_3.get_max_value())
            self.ui.lbMinBpValue.setText(self.chart_bp_3.get_min_value())

    def date_selected_weight(self):
        if self.ui.cbWeight.currentText() == '1 week':
            self.chart_weight_1 = ChartWeight(self.user, 1)
            self.weight_chart_2.hide()
            self.weight_chart_3.hide()
            self.weight_chart = self.chart_weight_1.get_chartview()
            self.layout_chart_weight.addWidget(self.weight_chart)
            self.ui.weightChart.setLayout(self.layout_chart_weight)
            self.ui.lbAvgWeightValue.setText(self.chart_weight_1.get_avg_value())
            self.ui.lbMaxWeightValue.setText(self.chart_weight_1.get_max_value())
            self.ui.lbMinWeightValue.setText(self.chart_weight_1.get_min_value())

        elif self.ui.cbWeight.currentText() == '1 month':
            self.chart_weight_2 = ChartWeight(self.user, 2)
            self.weight_chart.hide()
            self.weight_chart_3.hide()
            self.weight_chart_2 = self.chart_weight_2.get_chartview()
            self.layout_chart_weight.addWidget(self.weight_chart_2)
            self.ui.weightChart.setLayout(self.layout_chart_weight)
            self.ui.lbAvgWeightValue.setText(self.chart_weight_2.get_avg_value())
            self.ui.lbMaxWeightValue.setText(self.chart_weight_2.get_max_value())
            self.ui.lbMinWeightValue.setText(self.chart_weight_2.get_min_value())

        elif self.ui.cbWeight.currentText() == 'complete':
            self.chart_weight_3 = ChartWeight(self.user, 3)
            self.weight_chart.hide()
            self.weight_chart_2.hide()
            self.weight_chart_3 = self.chart_weight_3.get_chartview()
            self.layout_chart_weight.addWidget(self.weight_chart_3)
            self.ui.weightChart.setLayout(self.layout_chart_weight)
            self.ui.lbAvgWeightValue.setText(self.chart_weight_3.get_avg_value())
            self.ui.lbMaxWeightValue.setText(self.chart_weight_3.get_max_value())
            self.ui.lbMinWeightValue.setText(self.chart_weight_3.get_min_value())

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
            print(e+"email validation failed")
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
            print(e+"password validation failed.")
            return False

    def validate_height(self):
        try:
            input_int = int(self.ui.leSetHeight.text())
            if 140 < input_int < 250:
                return True
            else:
                return False
        except Exception as e:
            print(e+"height validation failed")
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
