from datetime import datetime
from PySide6.QtWidgets import QMainWindow
from src.views.user_management.WndRegistration import Ui_MainWindow

sex = ["male", "female", "other"]

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.leFirstName.textChanged.connect(self.validate_first_name)
        self.ui.leLastName.textChanged.connect(self.validate_last_nane)
        self.ui.dpBirthdate.dateChanged.connect(self.validate_birthday)
        self.ui.cbSex.addItems(sex)
        self.ui.leWeight.textChanged.connect(self.validate_weight)
        self.ui.sbHeight.valueChanged.connect(self.validate_height)
        self.ui.btnFinish.clicked.connect(self.finish_registration)

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
            return True
        else:
            return False

    def validate_weight(self):
        try:
            input = self.ui.leWeight.text()
            input_float = float(input)
            self.ui.leWeight.setStyleSheet("color: black;")
            return True
        except Exception as e:
            print(e)
            self.ui.leWeight.setStyleSheet("color: rgb(255, 0, 65);")
            return False

    def validate_height(self):
        try:
            input = self.ui.sbHeight.text().replace(",", ".").strip("'")
            input_float = float(input)
            if 1.40 < input_float < 2.30:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def finish_registration(self):
        if (self.validate_first_name() and self.validate_last_nane() and self.validate_birthday() and self.validate_weight() and self.validate_height()) == True:
            print("True")
        else:
            print("False")



