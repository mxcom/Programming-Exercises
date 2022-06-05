import re
import sys

from datetime import datetime
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6 import QtCore

from src.controllers.user_management.user_management import add_user
from src.models.user_management.user import User
from src.views.user_management.WndRegistration import Ui_MainWindow
from src.controllers.primary.primary import PrimaryWindow

sex = ["male", "female", "other"]
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
special_char = ['$', '@', '#', '%', '_', '-', '!']


class RegistrationWindow(QMainWindow, Ui_MainWindow):

    """
    Class provides functionalities to interact with ui
    """

    def __init__(self, parent=None):
        """
        Used to setup the ui and connect widgets with methods
        """
        super(RegistrationWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Settings for GUI
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.lbError.setVisible(False)
        self.ui.leEmail.textChanged.connect(self.validate_email)
        self.ui.lePassword.textChanged.connect(self.validate_passwd)
        self.ui.leConfirmPw.textChanged.connect(self.confirm_passwd)
        self.ui.btnNext.clicked.connect(self.next_page)
        self.ui.leFirstName.textChanged.connect(self.validate_first_name)
        self.ui.leLastName.textChanged.connect(self.validate_last_name)
        self.ui.dpBirthdate.dateChanged.connect(self.validate_birthday)
        self.ui.cbSex.addItems(sex)
        self.ui.cbSex.activated.connect(self.validate_sex)
        self.ui.leWeight.textChanged.connect(self.validate_weight)
        self.ui.sbHeight.valueChanged.connect(self.validate_height)
        self.ui.btnFinish.clicked.connect(self.finish_registration)
        self.ui.btnBack.clicked.connect(self.last_page)

        self.user = User()

    def validate_email(self):
        """
        Validate email based on regex

        Return
        ------
        bool
            True if regex and input correspond
            False if regex and input don't correspond
        """
        email = self.ui.leEmail.text()
        if re.fullmatch(regex, email):
            self.ui.leEmail.setStyleSheet("color: black;")
            self.user.set_email(self.ui.leEmail.text())
            return True
        else:
            self.ui.leEmail.setStyleSheet("color: rgb(255, 0, 65);")
            return False

    def validate_passwd(self):
        """
        Validates password based on define requirments

        Return
        ------
        bool
            True if password matches given requirements
            False if password don't match a requirement
        """
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
        """
        Confirm password has been entered correctly twice

        Return
        ------
        bool
            True if both passwords match
            False if both passwords don't match
        """
        if self.validate_passwd():
            passwd = self.ui.lePassword.text()
            confirm_passwd = self.ui.leConfirmPw.text()
            if passwd == confirm_passwd:
                self.ui.lbError.setVisible(False)
                self.user.set_passwd(self.ui.lePassword.text())
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
        """
        Validates that input for firstname if input > 2 characters

        Return
        ------
        bool
            True if input is > 3
            False if input is < 3
        """
        input = self.ui.leFirstName.text()
        if input == '' or len(input) < 3:
            self.ui.leFirstName.setStyleSheet("color: rgb(255, 0, 65);")
            return False
        else:
            self.user.set_first_name(self.ui.leFirstName.text())
            self.ui.leFirstName.setStyleSheet("color: black;")
            return True

    def validate_last_name(self):
        """
        Validates that input for lastname if input > 2 characters

        Return
        ------
        bool
            True if input is > 3
            False if input is < 3
        """
        input = self.ui.leLastName.text()
        if input == '' or len(input) < 3:
            self.ui.leLastName.setStyleSheet("color: rgb(255, 0, 65);")
            return False
        else:
            self.user.set_last_name(self.ui.leLastName.text())
            self.ui.leLastName.setStyleSheet("color: black;")
            return True

    def validate_birthday(self):
        """
        Validates that user is older than 18

        Return
        ------
        bool
            True if user is older than 18
            False if user is < 18
        """
        birthday = self.ui.dpBirthdate.date()
        if datetime.now().year - birthday.year() >= 18:
            self.user.set_birthday(self.ui.dpBirthdate.text())
            return True
        else:
            return False

    def validate_sex(self):
        self.user.set_sex(self.ui.cbSex.currentText())

    def validate_weight(self):
        """
        Checks if weight has been entered correctly

        Return
        ------
        bool
            True if weight is convertable to float
            False if weight isn't convertable to float
        """
        try:
            input = self.ui.leWeight.text()
            input_float = float(input)
            self.user.set_weight(self.ui.leWeight.text())
            self.ui.leWeight.setStyleSheet("color: black;")
            return True
        except Exception as e:
            print(e)
            self.ui.leWeight.setStyleSheet("color: rgb(255, 0, 65);")
            return False

    def validate_height(self):
        """
        Checks if height is between 140 and 250

        Return
        ------
        bool
            True if height is between 140 and 250
            False if height isn't between 140 and 250
        """
        try:
            input = self.ui.sbHeight.text().replace(",", ".").strip("'")
            input_int = int(input)
            if 140 < input_int < 250:
                self.user.set_height(input_int)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def next_page(self):
        """
        Switches the page from first login page to second
        """
        self.ui.leFirstName.setText(self.user.get_first_name())
        self.ui.leLastName.setText(self.user.get_last_name())
        self.ui.dpBirthdate.setDate(QtCore.QDate.fromString(self.user.get_birthday()))
        self.ui.cbSex.setCurrentText(self.user.get_sex())
        self.ui.leWeight.setText(self.user.get_weight())
        if self.user.get_height():
            self.ui.sbHeight.setValue(int(self.user.get_height()))
        else:
            self.ui.sbHeight.setValue(170)
        #
        if self.validate_email() and self.validate_passwd() and self.confirm_passwd() == True:
            self.ui.lbError.setVisible(False)
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.lbError.setStyleSheet("color: rgb(255, 0, 65);")
            self.ui.lbError.setText("Please fill out information")
            self.ui.lbError.setVisible(True)

    def last_page(self):
        """
        Switches the page from second login page to first
        """
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.leEmail.setText(self.user.get_email())
        self.ui.lePassword.setText(self.user.get_passwd())
        self.ui.leConfirmPw.setText(self.user.get_passwd())

    def finish_registration(self):
        """
        Checks all input for validation and creates new user
        """
        # Check if form has been filled correctly
        if self.validate_first_name() and self.validate_last_name() and self.validate_birthday() \
                and self.validate_weight() and self.validate_height() == True:
            self.user.set_sex(self.ui.cbSex.currentText())
            try:
                # add user to database
                add_user(self.user)
            except Exception as e:
                print(e)

        else:
            print("Fill out open fields")
