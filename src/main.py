import sys
import datetime
from PySide6.QtWidgets import QApplication, QMainWindow

from src.controllers.user_management.registration import RegistrationWindow
from src.controllers.user_management.login import LoginWindow
from src.controllers.user_management.email import send_mail
from src.controllers.user_management.user_management import get_user, add_user
from src.controllers.cryptography.cryptography import hash_passwd
from src.controllers.user_management.calorie_management import get_stat_kcal
from src.models.user_management.user import User


def main():
    # print("hello, world")
    # uncomment next line for email (and replace receiver mail)
    # send_mail('reciever@gmail.com')
    user = User(id='55', email='mxprivate@protonmail.com')
    get_stat_kcal(user, 2)

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
