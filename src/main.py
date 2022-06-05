import sys

from PySide6.QtWidgets import QApplication
from src.controllers.user_management.registration import MainWindow
from src.controllers.user_management.user_management import add_user
from src.models.user_management.user import User

def main():
    # user = User(email='max.semdner@gmail.com', first_name='Max', last_name='Semdner', sex='male', birthday='11.05.2001', height='1.81', weight='85')
    # add_user(user)
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
