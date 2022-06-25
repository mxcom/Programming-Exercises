import re, sys

from PySide6.QtWidgets import QMainWindow, QApplication, QStyle
from PySide6 import QtCore

from src.controllers.user_management.user_management import get_user, login
from src.controllers.user_management.admin_management import get_admin
from src.views.user_management.WndLogin import Ui_WndLogin
from src.controllers.primary.primary import PrimaryWindow
from src.controllers.primary.admin import AdminWindow
from src.controllers.user_management.registration import RegistrationWindow
from src.controllers.cryptography.cryptography import compare_passwd

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
admin_regex = re.compile(r'(A[1-9]{6})')


class LoginWindow(QMainWindow, Ui_WndLogin):
    """
    Class provides functionalities to interact with ui for login
    """

    def __init__(self, parent=None):
        """
        Used to setup the ui and connect widgets with methods
        """
        super(LoginWindow, self).__init__(parent)
        self.mw = None
        self.ui = Ui_WndLogin()
        self.ui.setupUi(self)

        # Settings for GUI
        self.ui.leEmail.textChanged.connect(self.validate_email)
        self.ui.btnLogin.clicked.connect(self.validate_login)

        # Change Window
        self.ui.btnSignup.clicked.connect(self.switch_to_registration)

    def switch_to_registration(self):
        self.mw = RegistrationWindow(LoginWindow=self)
        self.hide()
        self.mw.show()

    def validate_email(self):
        """
        Validate email based on regex

        Return
        ------
        bool
            True if regex and input correspond
            False if regex and input don't correspond
        """
        style_email = (u"QLineEdit{\n"
                       "border-bottom: 2px solid rgb(211, 201, 242);\n"
                       "}")
        self.ui.leEmail.setStyleSheet(style_email)
        email = self.ui.leEmail.text()
        if re.fullmatch(regex, email):
            self.ui.leEmail.setStyleSheet("color: black;")
            return True
        elif re.fullmatch(admin_regex, email):
            self.ui.leEmail.setStyleSheet("color: black;")
            return False
        else:
            self.ui.leEmail.setStyleSheet("color: rgb(255, 0, 65);")
            return False

    def validate_passwd(self):
        """
        validates password

        Return
        ------
        bool
            True if password is >= 8 chars
            False if password is > 8 chars
        """
        passwd = self.ui.lePassword.text()

        if len(passwd) < 8:
            return False
        else:
            return True

    def validate_admin(self):
        id = self.ui.leEmail.text()
        if re.fullmatch(admin_regex, id):
            self.ui.leEmail.setStyleSheet("color: black;")
            return True
        else:
            return False

    def validate_login(self):
        """
        Validates user login credentials using obove validate methods
        """
        if self.validate_email() and self.validate_passwd():
            try:
                user = get_user(self.ui.leEmail.text())

                if compare_passwd(self.ui.lePassword.text(), user.get_passwd()):
                    login(user)
                    self.hide()
                    self.mw = PrimaryWindow(user, LoginWindow=self)
                    self.mw.show()
                else:
                    print("wrong email or password")
            except Exception as e:
                print(e)
        elif self.validate_admin() and self.validate_passwd():
            try:
                admin = get_admin(self.ui.leEmail.text())

                if compare_passwd(self.ui.lePassword.text(), admin.get_password()):
                    self.destroy()
                    self.mw = AdminWindow(admin)
                    self.mw.show()
                else:
                    print("wrong identifier or password")
            except Exception as e:
                print(e)
        else:
            print("could not validate")
