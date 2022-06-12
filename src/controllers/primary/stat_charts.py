from PySide6.QtCharts import QLineSeries, QChart, QChartView, QBarSeries, QBarSet
from PySide6.QtGui import QPen, QColor, Qt, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout


def create_chart():
    #series = QListSries()
    #series.append(0, 6)
    #series.append(2, 4)
    #series.append(4, 10)
    #series.append(5, 3)
    #series.append(6, 7)

    set0 = QBarSet("kcal")
    set0 << 2000 << 2400 << 1900 << 2100 << 2000 << 2350 << 1900

    series = QBarSeries()
    series.append(set0)
    series.setBarWidth(series.count())

    chart = QChart()
    chart.addSeries(series)
    chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.setTitle("Test Title")
    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)
   

    chartview = QChartView(chart)
    chartview.setRenderHint(QPainter.Antialiasing)
    return chartview
