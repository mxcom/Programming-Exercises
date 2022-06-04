from datetime import datetime
from PySide6.QtWidgets import QMainWindow
from src.views.user_management.WndRegistration import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.leFirstName.textChanged.connect(self.validate_first_name)
        self.ui.leLastName.textChanged.connect(self.validate_last_nane)
        self.ui.dpBirthdate.dateChanged.connect(self.validate_birthday)
        # self.ui.btnFinish.clicked.connect(self.method)

    def validate_first_name(self):
        input = self.ui.leFirstName.text()
        if input == '' or len(input) < 3:
            self.ui.leFirstName.setStyleSheet("color: rgb(255, 0, 65);")
            return False
        else:
            self.ui.leFirstName.setStyleSheet("color: black;")
            return True

    def validate_last_nane(self):
        input = self.ui.leLastName.text()
        if input == '' or len(input) < 3:
            self.ui.leLastName.setStyleSheet("color: rgb(255, 0, 65);")
            return False
        else:
            self.ui.leLastName.setStyleSheet("color: black;")
            return True

    def validate_birthday(self):
        birthday = self.ui.dpBirthdate.date()
        if datetime.now().year - birthday.year() >= 18:
            return False
        else:
            return True

