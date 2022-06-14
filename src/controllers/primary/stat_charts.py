import datetime

from PySide6.QtCharts import QLineSeries, QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis, \
    QPercentBarSeries
from PySide6.QtGui import QPen, QColor, Qt, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout
from datetime import date
import calendar
from src.controllers.user_management.calorie_management import get_stat_kcal
from src.models.user_management.user import User
from src.controllers.user_management.calc_kcal import calc_kcal


class Chart():
    def __init__(self, user, period):
        # Create Set of Kcal for one week
        self.results = get_stat_kcal(user, period)

        # results = QBarSet("kcal")
        # for i in cursor.fetchall():
        #    results << i[0]
        self.set0 = QBarSet("kcal")
        for i in self.results:
            self.set0 << self.results[i]

        self.set0.setColor(QColor(0x7A64BD))

        # Create Series where given set is added
        self.series = QBarSeries()
        self.series.append(self.set0)
        self.series.setBarWidth(self.series.count())

        # create chart
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)

        curr_date = datetime.datetime.today()
        temp_date = calendar.day_name[curr_date.weekday()]
        categories = [temp_date[0:3]]
        i = 0
        myrange = self.set0.count() - 1
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
        self.axisX.append(categories)
        self.axisY = QValueAxis()
        self.axisY.setRange(0, max(self.results))
        self.chart.setAxisY(self.axisY)

        self.chartview = QChartView(self.chart)

    def get_chartview(self):
        return self.chartview

    def get_max_value(self):
        return str(max(self.results))

    def get_min_value(self):
        return str(min(self.results))

    def get_avg_value(self):
        return str(sum(self.results) / len(self.results))
