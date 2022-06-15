from datetime import datetime
import re


from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QTableWidgetItem
from src.views.primary.WndAdmin import Ui_WndAdmin
from src.controllers.user_management.user_management import get_all_users


class PrimaryWindow(QMainWindow, Ui_WndAdmin):

    def __init__(self, parent=None):
        super(PrimaryWindow, self).__init__(parent)
        self.ui = Ui_WndAdmin()
        self.ui.setupUi(self)

        users = get_all_users()
        self.fill_table(users)

    def fill_table(self, users):
        row = 0
        self.ui.twUsers.setRowCount(len(users))
        for i in users:
            self.ui.twUsers.setItem(row, 0, QTableWidgetItem(i["ID"]))
            self.ui.twUsers.setItem(row, 1, QTableWidgetItem(i["Email"]))
            self.ui.twUsers.setItem(row, 2, QTableWidgetItem(i["FirstName"]))
            self.ui.twUsers.setItem(row, 3, QTableWidgetItem(i["LastName"]))
            self.ui.twUsers.setItem(row, 4, QTableWidgetItem(i["Sex"]))
            self.ui.twUsers.setItem(row, 5, QTableWidgetItem(i["Birthday"]))
            self.ui.twUsers.setItem(row, 6, QTableWidgetItem(i["Height"]))
            self.ui.twUsers.setItem(row, 7, QTableWidgetItem(i["Password"]))
            row = row + 1


