import datetime

from PySide6.QtCharts import QLineSeries, QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis
from PySide6.QtGui import QPen, QColor, Qt, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout
from datetime import date
import calendar


def create_chart():
    # Create Set of Kcal for one week
    set0 = QBarSet("kcal")
    set0 << 2000 << 2400 << 1900 << 2100 << 2000 << 2350 << 1900
    set0.setColor(QColor(0x7A64BD))

    # Create Series where given set is added
    series = QBarSeries()
    series.append(set0)
    series.setBarWidth(series.count())

    pen = QPen()
    pen.setColor(QColor(0x7A64BD))

    # Create Axis

    curr_date = datetime.datetime.today()
    temp_date = calendar.day_name[curr_date.weekday()]
    categories = [temp_date[0:3]]
    i = 0
    for i in range(6):
        curr_date += datetime.timedelta(days=1)
        temp_date = calendar.day_name[curr_date.weekday()]
        categories.append(temp_date[0:3])
        i += 1

    axisX = QBarCategoryAxis()
    axisX.append(categories)
    series.attachAxis(axisX)

    # Create chart and set properties
    chart = QChart()
    chart.addSeries(series)
    chart.addAxis(axisX, Qt.AlignBottom)
    chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)


    # Create Chart View and add created chart to chart view
    chartview = QChartView(chart)
    chartview.setRenderHint(QPainter.Antialiasing)
    return chartview
