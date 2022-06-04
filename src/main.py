import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from src.controllers.user_management.registration import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    # user_management.add_user('max.semder@gmail.com', 'Max', 'Semdner', 'Male', datetime.datetime(2001, 11, 5), args[1])


if __name__ == "__main__":
    main()
