import datetime

from PySide6.QtCharts import QLineSeries, QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis, \
    QPercentBarSeries, QSplineSeries
from PySide6.QtGui import QPen, QColor, Qt, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout
from datetime import date
import calendar
from src.controllers.user_management.calorie_management import get_stat_kcal
from src.models.user_management.user import User
from src.controllers.user_management.calc_kcal import calc_kcal


class ChartKcal:
    def __init__(self, user, period):
        # Create Set of Kcal for one week
        self.results = get_stat_kcal(user, period)

        if period == 1:
            # results = QBarSet("kcal")
            # for i in cursor.fetchall():
            #    results << i[0]
            self.set1 = QBarSet("kcal")

            for i in self.results:
                self.set1 << i

            self.set1.setColor(QColor(0x7A64BD))

            # Create Series where given set is added
            self.series = QBarSeries()
            self.series.append(self.set1)
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
            myrange = self.set1.count() - 1
            for i in range(myrange):
                curr_date -= datetime.timedelta(days=1)
            temp_date = calendar.day_name[curr_date.weekday()]
            categories.append(temp_date[0:3])
            i += 1

            self.axisX = QBarCategoryAxis()
            self.axisX.append(categories[::-1])
            self.axisY = QValueAxis()
            self.axisY.setRange(0, max(self.results))
            self.axisY.setLabelFormat("%.0f")
            self.chart.setAxisY(self.axisY)
            self.chart.setAxisX(self.axisX)

            self.chartview = QChartView(self.chart)
        elif period == 2:
            # results = QBarSet("kcal")
            # for i in cursor.fetchall():
            #    results << i[0]
            self.set2 = QBarSet("kcal")

            for i in self.results:
                self.set2 << i

            self.set2.setColor(QColor(0x7A64BD))

            # Create Series where given set is added
            self.series = QBarSeries()
            self.series.append(self.set2)
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
            myrange = self.set2.count() - 1
            for i in range(myrange):
                curr_date -= datetime.timedelta(days=1)
            temp_date = calendar.day_name[curr_date.weekday()]
            categories.append(temp_date[0:3])
            i += 1

            self.axisX = QBarCategoryAxis()
            self.axisX.append(categories[::-1])
            self.axisY = QValueAxis()
            self.axisY.setRange(0, max(self.results))
            self.axisY.setLabelFormat("%.0f")
            self.chart.setAxisY(self.axisY)
            self.chart.setAxisX(self.axisX)

            self.chartview = QChartView(self.chart)

        elif period == 3:
            self.series = QSplineSeries()

            j = 0
            for i in self.results:
                self.series.append(j, float(self.results[j]))
                j += 1

            self.series.setColor(QColor(0x7A64BD))

            pen = QPen()
            pen.setColor(QColor(0x7A64BD))
            pen.setWidth(2)

            self.series.setPen(pen)
            self.series.setBestFitLinePen(pen)

            self.chart = QChart()
            self.chart.addSeries(self.series)
            self.chart.setAnimationOptions(QChart.SeriesAnimations)
            self.chart.legend().setVisible(False)

            self.axisY = QValueAxis()
            self.axisY.setRange(0, max(self.results))
            self.axisY.setLabelFormat("%.0f")
            self.chart.setAxisY(self.axisY)

            self.chartview = QChartView(self.chart)

    def get_chartview(self):
        return self.chartview

    def get_max_value(self):
        return str(max(self.results))

    def get_min_value(self):
        return str(min(self.results))

    def get_avg_value(self):
        return str(int(sum(self.results) / len(self.results)))
