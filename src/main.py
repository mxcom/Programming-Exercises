import sys
import datetime
from PySide6.QtWidgets import QApplication, QMainWindow

from src.controllers.user_management.registration import RegistrationWindow
from src.controllers.user_management.login import LoginWindow
from src.controllers.user_management.email import send_mail
from src.controllers.user_management.user_management import get_user, add_user, insert_random
from src.controllers.cryptography.cryptography import hash_passwd
from src.controllers.user_management.calorie_management import *
from src.models.user_management.user import User
from src.controllers.user_management.calorie_management import add_dummy_kcal, add_dummy_bp, add_dummy_steps, add_dummy_weight


def main():
    # print(hash_passwd("HelloWorld"))
    # print("hello, world")
    # uncomment next line for email (and replace receiver mail)
    # send_mail('reciever@gmail.com')

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec()
    # add_dummy_kcal()
    # add_dummy_bp()
    # add_dummy_steps()
    # add_dummy_weight()

if __name__ == "__main__":
    main()
