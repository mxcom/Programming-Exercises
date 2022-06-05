import re

from datetime import datetime
from PySide6.QtWidgets import QMainWindow
from src.views.user_management.WndRegistration import Ui_MainWindow

sex = ["male", "female", "other"]
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
special_char = ['$', '@', '#', '%', '_', '-', '!']


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lbError.setVisible(False)
        self.ui.leEmail.textChanged.connect(self.validate_email)
        self.ui.lePassword.textChanged.connect(self.validate_passwd)
        self.ui.leConfirmPw.textChanged.connect(self.confirm_passwd)
        self.ui.leFirstName.textChanged.connect(self.validate_first_name)
        self.ui.leLastName.textChanged.connect(self.validate_last_nane)
        self.ui.dpBirthdate.dateChanged.connect(self.validate_birthday)
        self.ui.cbSex.addItems(sex)
        self.ui.leWeight.textChanged.connect(self.validate_weight)
        self.ui.sbHeight.valueChanged.connect(self.validate_height)
        self.ui.btnFinish.clicked.connect(self.finish_registration)

    def validate_email(self):
        email = self.ui.leEmail.text()
        print("asdf")
        if re.fullmatch(regex, email):
            self.ui.leEmail.setStyleSheet("color: black;")
            return True
        else:
            self.ui.leEmail.setStyleSheet("color: rgb(255, 0, 65);")
            return False

    def validate_passwd(self):
        self.ui.lbError.setVisible(False)
        passwd = self.ui.lePassword.text()

        # Password needs to contain at least 1 uppercase letter
        if not any(char.isupper() for char in passwd):
            self.ui.lbError.setVisible(True)
            self.ui.lbError.setStyleSheet("color: rgb(255, 0, 65);")
            self.ui.lbError.setText("Password must contain at least 1 uppercase letter")
            return False

        # Password needs to contain at least 1 lowercase letter
        if not any(char.islower() for char in passwd):
            self.ui.lbError.setVisible(True)
            self.ui.lbError.setStyleSheet("color: rgb(255, 0, 65);")
            self.ui.lbError.setText("Password must contain at least 1 lowercase letter")
            return False

        # Password needs to contain at least 1 digit
        if not any(char.isdigit() for char in passwd):
            self.ui.lbError.setVisible(True)
            self.ui.lbError.setStyleSheet("color: rgb(255, 0, 65);")
            self.ui.lbError.setText("Password must contain at least 1 digit")
            return False

        # Password needs to contain at least 1 special character
        if not any(char in special_char for char in passwd):
            self.ui.lbError.setVisible(True)
            self.ui.lbError.setStyleSheet("color: rgb(255, 0, 65);")
            self.ui.lbError.setText("Password must contain at least special character")
            return False

        # Password needs to be >= 8 characters
        if len(passwd) < 8:
            self.ui.lbError.setVisible(True)
            self.ui.lbError.setStyleSheet("color: rgb(255, 0, 65);")
            self.ui.lbError.setText("Password must be at least 8 characters long")
            return False

        self.ui.lbError.setVisible(False)
        return True

    def confirm_passwd(self):
        if self.validate_passwd():
            passwd = self.ui.lePassword.text()
            confirm_passwd = self.ui.leConfirmPw.text()
            if passwd == confirm_passwd:
                self.ui.lbError.setVisible(False)
                return True
            else:
                self.ui.lbError.setVisible(True)
                self.ui.lbError.setStyleSheet("color: rgb(255, 0, 65);")
                self.ui.lbError.setText("Passwords don't match")
                return False
        else:
            self.ui.lbError.setVisible(True)
            self.ui.lbError.setStyleSheet("color: rgb(255, 0, 65);")
            self.ui.lbError.setText("Passwords don't match")
            return False

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



