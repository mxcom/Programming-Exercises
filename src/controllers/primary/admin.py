from datetime import datetime
import re


from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QTableWidgetItem, QTableWidget
from PySide6 import QtCore
from src.views.primary.WndAdmin import Ui_WndAdmin
from src.controllers.user_management.user_management import get_all_users, update_email, update_first_name, update_sex, \
    update_birthday, update_height, update_passwd
from src.controllers.cryptography.cryptography import hash_passwd
from src.models.user_management.user import User

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

        self.previous = None
        self.ui.twUsers.itemClicked.connect(self.item_selected)
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
                previous_email = self.previous
                self.ui.twUsers.currentItem().setText(self.previous)
                print(e)

        if column == 1:
            try:
                if re.fullmatch(regex_email, self.ui.twUsers.currentItem().text()):
                    user = User(email=self.previous)
                    cell = self.ui.twUsers.currentItem().text()
                    update_email(user, cell)
                else:
                    self.ui.twUsers.currentItem().setText(self.previous)
                    return
            except Exception as e:
                self.ui.twUsers.currentItem().setText(self.previous)
                print(e)

        if column == 2:
            try:
                if re.fullmatch(regex_name, self.ui.twUsers.currentItem().text()):
                    id = self.ui.twUsers.item(self.ui.twUsers.currentRow(), 0).text()
                    cell = self.ui.twUsers.currentItem().text()
                    user = User(id=id, first_name=self.previous)
                    update_first_name(user, cell)
                else:
                    self.ui.twUsers.currentItem().setText(self.previous)
                    return
            except Exception as e:
                self.ui.twUsers.currentItem().setText(self.previous)
                print(e)

        if column == 3:
            try:
                if re.fullmatch(regex_name, self.ui.twUsers.currentItem().text()):
                    id = self.ui.twUsers.item(self.ui.twUsers.currentRow(), 0).text()
                    cell = self.ui.twUsers.currentItem().text()
                    user = User(id=id, last_name=self.previous)
                    update_first_name(user, cell)
                else:
                    self.ui.twUsers.currentItem().setText(self.previous)
                    return
            except Exception as e:
                self.ui.twUsers.currentItem().setText(self.previous)
                print(e)

        if column == 4:
            try:
                if self.ui.twUsers.currentItem().text() == 'male':
                    id = self.ui.twUsers.item(self.ui.twUsers.currentRow(), 0).text()
                    user = User(id=id, last_name=self.previous)
                    update_sex(user, 'male')
                elif self.ui.twUsers.currentItem().text() == 'female':
                    id = self.ui.twUsers.item(self.ui.twUsers.currentRow(), 0).text()
                    user = User(id=id, last_name=self.previous)
                    update_sex(user, 'female')
                else:
                    self.ui.twUsers.currentItem().setText(self.previous)
                    return
            except Exception as e:
                self.ui.twUsers.currentItem().setText(self.previous)
                print(e)

        if column == 5:
            try:
                id = self.ui.twUsers.item(self.ui.twUsers.currentRow(), 0).text()
                user = User(id=id, birthday=self.previous)
                cell = self.ui.twUsers.currentItem().text()
                date = datetime.strptime(cell, "%Y-%m-%d")
                update_birthday(user, date)
            except Exception as e:
                self.ui.twUsers.currentItem().setText(self.previous)
                print(e)

        if column == 6:
            try:
                id = self.ui.twUsers.item(self.ui.twUsers.currentRow(), 0).text()
                user = User(id=id, height=self.previous)
                cell = self.ui.twUsers.currentItem().text()
                update_height(user, cell)
            except Exception as e:
                self.ui.twUsers.currentItem().setText(self.previous)
                print(e)

        if column == 7:
            try:
                cell = self.ui.twUsers.currentItem().text()
                # Password needs to contain at least 1 uppercase letter
                if not any(char.isupper() for char in cell):
                    self.ui.twUsers.currentItem().setText(self.previous)
                    return

                # Password needs to contain at least 1 lowercase letter
                if not any(char.islower() for char in cell):
                    self.ui.twUsers.currentItem().setText(self.previous)
                    return

                # Password needs to contain at least 1 digit
                if not any(char.isdigit() for char in cell):
                    self.ui.twUsers.currentItem().setText(self.previous)
                    return

                # Password needs to contain at least 1 special character
                if not any(char in special_char for char in cell):
                    self.ui.twUsers.currentItem().setText(self.previous)
                    return

                # Password needs to be >= 8 characters
                if len(cell) < 8:
                    self.ui.twUsers.currentItem().setText(self.previous)
                    return

                id = self.ui.twUsers.item(self.ui.twUsers.currentRow(), 0).text()
                user = User(id=id, passwd=self.previous)
                update_passwd(user, self.ui.twUsers.currentItem().text())
            except Exception as e:
                print(e)

    def item_selected(self):
        self.previous = str(self.ui.twUsers.currentItem().text())







