import datetime

from PySide6.QtCharts import QLineSeries, QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PySide6.QtGui import QPen, QColor, Qt, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout
from datetime import date
import calendar
from src.controllers.user_management.calorie_management import get_stat_kcal
from src.models.user_management.user import User


def create_chart(user, period):
    # Create Set of Kcal for one week
    set0 = get_stat_kcal(user, period)
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
    myrange = set0.count()-1
    for i in range(myrange):
        curr_date += datetime.timedelta(days=1)
        temp_date = calendar.day_name[curr_date.weekday()]
        categories.append(temp_date[0:3])
        i += 1

    axisX = QBarCategoryAxis()
    axisX.append(categories)
    series.attachAxis(axisX)

    axisY = QValueAxis()
    axisY.setRange(0, 2400)
    axisY.setLabelFormat("%.0f")
    series.attachAxis(axisY)

    # Create chart and set properties
    chart = QChart()
    chart.addSeries(series)
    chart.addAxis(axisX, Qt.AlignBottom)
    chart.addAxis(axisY, Qt.AlignLeft)
    chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.legend().setVisible(False)


    # Create Chart View and add created chart to chart view
    chartview = QChartView(chart)
    chartview.setRenderHint(QPainter.Antialiasing)
    return chartview
