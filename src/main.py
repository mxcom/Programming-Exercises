import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from src.controllers.user_management.registration import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
