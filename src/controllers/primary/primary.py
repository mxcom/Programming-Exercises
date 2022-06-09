from datetime import datetime
from tkinter.ttk import Style

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QFont, Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QSizePolicy

from PySide6 import QtGui, QtCore
from PySide6 import QtCore
from PySide6.QtGui import QPixmap

from src.views.primary.WndMain import Ui_WndMain
from src.views.primary.uiFunctions import UIFunctions
import src.views.icons.rc_icons



class PrimaryWindow(QMainWindow, Ui_WndMain):

    def __init__(self, parent=None):
        super(PrimaryWindow, self).__init__(parent)
        self.ui = Ui_WndMain()
        self.ui.setupUi(self)

        self.ui.btnToggle.clicked.connect(lambda: UIFunctions.toggleMenu(self,200, True))

        # Add icons to buttons


