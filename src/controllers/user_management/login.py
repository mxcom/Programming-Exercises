import re, sys

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6 import QtCore

from src.controllers.user_management.user_management import search_user, validate_user
from src.views.user_management.WndLogin import Ui_WndLogin
from src.views.user_management.WndRegistration import Ui_WndRegistration
from src.controllers.user_management.registration import RegistrationWindow

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-a-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


class LoginWindow(QMainWindow, Ui_WndLogin):
    """
    Class provides functionalities to interact with ui for login
    """
    def __init__(self, parent=None):
        """
        Used to setup the ui and connect widgets with methods
        """
        super(LoginWindow, self).__init__(parent)
        self.ui = Ui_WndLogin()
        self.ui.setupUi(self)

        # Settings for GUI
        self.ui.leEmail.textChanged.connect(self.validate_email)
        self.ui.btnLogin.clicked.connect(self.validate_login)

        # Change Window
        self.ui.btnSignup.clicked.connect(self.window_switch)

    def window_switch(self):
        self.destroy()
        self.mw = RegistrationWindow()
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
        email = self.ui.leEmail.text()
        if re.fullmatch(regex, email):
            self.ui.leEmail.setStyleSheet("color: black;")
            return True
        else:
            self.ui.leEmail.setStyleSheet("color: rgb(255, 0, 65);")
            return False

    def validate_passwd(self):
        passwd = self.ui.lePassword.text()

        if len(passwd) < 8:
            return False
        else:
            return True

    def validate_login(self):
        if self.validate_email() and self.validate_passwd() == True:
            try:
                email = self.ui.leEmail.text()
                passwd = self.ui.lePassword.text()
                if search_user(email):
                    print("user found")
                else:
                    print("user not found")

                if validate_user(email, passwd):
                    print("same passwd")
                else:
                    print("not same passwd")
            except Exception as e:
                print(e)