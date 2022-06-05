import sys

from PySide6.QtWidgets import QApplication
from src.controllers.user_management.registration import RegistrationWindow

def main():
    app = QApplication(sys.argv)

    window = RegistrationWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
