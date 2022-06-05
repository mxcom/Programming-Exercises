import sys

from PySide6.QtWidgets import QApplication

# from src.controllers.user_management.registration import RegistrationWindow
from src.controllers.user_management.login import LoginWindow


def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
