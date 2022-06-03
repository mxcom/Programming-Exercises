import sys
import datetime

from src.controllers.user_management import user_management


def main(args):
    user_management.add_user('max.semder@gmail.com', 'Max', 'Semdner', 'Male', datetime.datetime(2001, 11, 5), args[1])


if __name__ == "__main__":
    main(sys.argv)
