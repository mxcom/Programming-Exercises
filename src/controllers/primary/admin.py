from datetime import datetime
import re


from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QTableWidgetItem, QTableWidget
from PySide6 import QtCore
from src.views.primary.WndAdmin import Ui_WndAdmin
from src.controllers.user_management.user_management import get_all_users
from src.controllers.cryptography.cryptography import hash_passwd

regex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
regex_name = re.compile('[A-Z]+[a-z]*')
special_char = ['$', '@', '#', '%', '_', '-', '!']

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

        self.selected = self.ui.twUsers.itemClicked.connect(self.item_selected)
        self.ui.twUsers.itemChanged.connect(self.item_changed)
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
            for item in match:
                item.setSelected(True)

    def item_changed(self):
        column = self.ui.twUsers.currentColumn()

        if column == 0:
            try:
                cell = int(self.ui.twUsers.currentItem().text())
            except Exception as e:
                print("input not valid")
                print(e)

        if column == 1:
            try:
                if re.fullmatch(regex_email, self.ui.twUsers.currentItem().text()):
                    cell = self.ui.twUsers.currentItem().text()
                else:
                    print("input not valid")
                    self.fill_table()
            except Exception as e:
                self.fill_table()
                print(e)

        if column == 2:
            try:
                if re.fullmatch(regex_name, self.ui.twUsers.currentItem().text()):
                    cell = self.ui.twUsers.currentItem().text()
                else:
                    print("input not valid")
            except Exception as e:
                print("input not valid")
                print(e)

        if column == 3:
            try:
                if re.fullmatch(regex_name, self.ui.twUsers.currentItem().text()):
                    cell = self.ui.twUsers.currentItem().text()
                else:
                    print("input not valid")
            except Exception as e:
                print("input not valid")
                print(e)

        if column == 4:
            try:
                if self.ui.twUsers.currentItem().text() == 'male':
                    cell = self.ui.twUsers.currentItem().text()
                elif self.ui.twUsers.currentItem().text() == 'female':
                    cell = self.ui.twUsers.currentItem().text()
                else:
                    print("input not valid")
            except Exception as e:
                print("input not valid")
                print(e)

        if column == 6:
            try:
                cell = int(self.ui.twUsers.currentItem().text())
            except Exception as e:
                print("input not valid")
                print(e)

        if column == 7:
            try:
                cell = self.ui.twUsers.currentItem().text()

                # Password needs to contain at least 1 uppercase letter
                if not any(char.isupper() for char in cell):
                    print("input not valid")
                    return

                # Password needs to contain at least 1 lowercase letter
                if not any(char.islower() for char in cell):
                    print("input not valid")
                    return

                # Password needs to contain at least 1 digit
                if not any(char.isdigit() for char in cell):
                    print("input not valid")
                    return

                # Password needs to contain at least 1 special character
                if not any(char in special_char for char in cell):
                    print("input not valid")
                    return

                # Password needs to be >= 8 characters
                if len(cell) < 8:
                    print("input not valid")
                    return

                hashed = hash_passwd(cell).decode("utf-8")
                self.ui.twUsers.currentItem().setText("asdf")
            except Exception as e:
                print("input not valid")
                print(e)

    def item_selected(self):
        selection = self.ui.twUsers.currentItem().text()
        return selection







