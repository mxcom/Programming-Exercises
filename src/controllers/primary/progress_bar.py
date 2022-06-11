from PySide6 import QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class CircularProgress(QWidget):
    def __init__(self, start_value, end_value, max_value):
        QWidget.__init__(self)

        # Properties
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 15
        self.progress_round_cap = True
        self.progress_color = 0x6437ED
        self.progress_color_background = 0x2E196E
        self.max_value = max_value  # Has to be changed later to max amount of daily calories
        self.font_size = 15
        self.font_family = "Sergoe UI Black"
        self.slash_text = "/"
        self.suffix = "\nkcal"
        self.text_color = 0x000000
        self.enable_shadow = True

        self.resize(self.width, self.height)

        # Animation of the progress
        self.animation = QtCore.QVariantAnimation(self)
        self.animation.setDuration(2000)
        self.animation.setStartValue(start_value)
        self.animation.setEndValue(end_value)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.valueChanged.connect(self.update)
        self.animation.start()

    def set_value(self, value):
        self.value = value
        self.repaint()

    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value
        value_background = self.max_value

        # Painter
        paint = QPainter()
        # self.setFont(QFont(self.font_family, self.font_size))
        paint.begin(self)
        # Depending on where I put the statment the either way the result is not satesfying
        self.setFont(QFont(self.font_family, self.font_size))
        paint.setRenderHint(QPainter.Antialiasing)

        # Create Rectangle
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # Pen
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)

        if self.progress_round_cap:
            pen.setCapStyle(Qt.RoundCap)

        # Pen Background
        pen_background = QPen()
        pen_background.setColor(QColor(self.progress_color_background))
        pen_background.setWidth(self.progress_width)

        if self.progress_round_cap:
            pen_background.setCapStyle(Qt.RoundCap)

        # Creat Arc Background
        paint.setPen(pen_background)
        paint.drawArc(margin, margin, width, height, -90 * 16, -self.max_value * 16)

        # Creat Arc animationated
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, (-self.animation.currentValue() * 360 / self.max_value) * 16)


        # Create Text
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f"{self.animation.currentValue()}{self.slash_text}{self.max_value}{self.suffix}")

        paint.end()
