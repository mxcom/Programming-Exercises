from datetime import datetime
import re


from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QTableWidgetItem
from PySide6 import QtCore
from src.views.primary.WndAdmin import Ui_WndAdmin
from src.controllers.user_management.user_management import get_all_users


class AdminWindow(QMainWindow, Ui_WndAdmin):

    def __init__(self, admin, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.ui = Ui_WndAdmin()
        self.ui.setupUi(self)
        self.admin = admin

        self.ui.twUsers.setColumnWidth(0, 10)
        self.ui.twUsers.setColumnWidth(1, 200)
        self.ui.twUsers.setColumnWidth(2, 150)
        self.ui.twUsers.setColumnWidth(3, 150)
        self.ui.twUsers.setColumnWidth(4, 60)
        self.ui.twUsers.setColumnWidth(5, 90)
        self.ui.twUsers.setColumnWidth(6, 60)
        self.ui.twUsers.setColumnWidth(7, 250)

        self.ui.lbName.setText(self.admin.get_identifier())

        users = get_all_users()
        self.fill_table(users)

        self.ui.leSearch.textChanged.connect(self.search_user)

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

    def search_user(self):
        self.ui.twUsers.setCurrentItem(None)

        if not self.ui.leSearch.text():
            return

        match = self.ui.twUsers.findItems(self.ui.leSearch.text(), QtCore.Qt.MatchContains)
        if match:
            item = match[0]
            self.ui.twUsers.setCurrentItem(item)



