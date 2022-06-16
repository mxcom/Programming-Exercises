import datetime

from PySide6.QtCharts import QLineSeries, QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis, \
    QPercentBarSeries
from PySide6.QtGui import QPen, QColor, Qt, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout
from datetime import date
import calendar
from src.controllers.user_management.calorie_management import *


class ChartBp:
    def __init__(self, user, period):
        self.results_sys = get_stat_sys(user, period)
        self.results_dia = get_stat_dia(user, period)
        print(self.results_dia)
        print(self.results_sys)

        self.set_sys = QBarSet("Systolic")
        self.set_dia = QBarSet("Diastolic")
        self.set_sys.append(self.results_sys)
        self.set_dia.append(self.results_dia)

        self.set_sys.setColor(QColor(0x7A64BD))
        self.set_dia.setColor(QColor(0xD3C9F2))

        # Create Series where given set is added
        self.series = QBarSeries()
        self.series.append(self.set_dia)
        self.series.append(self.set_sys)
        self.series.setBarWidth(self.series.count()/2)

        # create chart
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.legend().setVisible(False)

        curr_date = datetime.datetime.today()
        temp_date = calendar.day_name[curr_date.weekday()]
        categories = [temp_date[0:3]]
        i = 0
        myrange = self.set_sys.count() - 1
        for i in range(myrange):
            curr_date -= datetime.timedelta(days=1)
            temp_date = calendar.day_name[curr_date.weekday()]
            categories.append(temp_date[0:3])
            i += 1
        '''
        self.axis = QBarCategoryAxis()
        self.axis.append(categories)
        self.chart.createDefaultAxes()
        self.chart.setAxisX(self.axis, self.series)
        self.chart.setAxisY(self.axis)'''

        self.axisX = QBarCategoryAxis()
        self.axisX.append(categories[::-1])
        self.axisY = QValueAxis()
        self.axisY.setRange(0, max(self.results_sys))
        self.axisY.setLabelFormat("%.0f")
        self.chart.setAxisY(self.axisY)
        self.chart.setAxisX(self.axisX)

        self.chartview = QChartView(self.chart)

    def get_chartview(self):
        return self.chartview

    def get_max_value(self):
        return str(max(self.results_sys)) + "/" + str(max(self.results_dia))

    def get_min_value(self):
        return str(min(self.results_sys)) + "/" + str(min(self.results_dia))

    def get_avg_value(self):
        return str(int(sum(self.results_sys) / len(self.results_sys))) + "/" + str(int(sum(self.results_dia) / len(self.results_dia)))
