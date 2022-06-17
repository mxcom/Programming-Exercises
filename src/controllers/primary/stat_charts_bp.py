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

        self.set_sys = QBarSet("Systolic")
        self.set_dia = QBarSet("Diastolic")

        for i in self.results_sys:
            self.set_sys << i

        for i in self.results_dia:
            self.set_dia << i

        self.set_sys.setColor(QColor(0x7A64BD))
        self.set_dia.setColor(QColor(0xD3C9F2))

        # Create Series where given set is added
        self.series = QBarSeries()
        self.series.append(self.set_dia)
        self.series.append(self.set_sys)
        self.series.setBarWidth(self.series.count())

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
    #    self.axisY.setRange(0, max(self.results_sys))
        self.setRange
        self.axisY.setLabelFormat("%.0f")
        self.chart.setAxisY(self.axisY)
        self.chart.setAxisX(self.axisX)

        self.chartview = QChartView(self.chart)

    def setRange():
        if len(self.results) > 0:
            x = float(max(self.results))    
        else:
            x= float(0)
        self.axisY.setRange(float(0,x))

    def get_chartview(self):
        return self.chartview

    def get_max_value(self):
        if len(self.results_sys) > 0 & len(self.results_dia)  > 0 :
           return str(max(self.results_sys)) + "/" + str(max(self.results_dia))

        else:
            return "Keine Werte Vorhanden"


    def get_min_value(self):
        if len(self.results_sys) > 0 & len(self.results_dia)  > 0 :
           return str(min(self.results_sys)) + "/" + str(min(self.results_dia))

        else:
            return "Keine Werte Vorhanden"

    def get_avg_value(self):
        if len(self.results_sys) > 0 & len(self.results_dia)  > 0 :
            return str(int(sum(self.results_sys) / len(self.results_sys))) + "/" + str(int(sum(self.results_dia) / len(self.results_dia)))
        else:
            return "Keine Werte Vorhanden"
            
    def get_chartview(self):
        return self.chartview