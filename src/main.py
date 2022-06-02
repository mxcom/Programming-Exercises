import sys
import datetime
from src.controllers import database
from src.controllers.user_management import user_management

def main(args):
    db = database.connection(args[1], args[2])
    user_management.add_user(db, 'mxprivate@protonmail.com', 'Max', 'Semdner', 'Male', datetime.datetime(2001, 11, 5), args[3])

if __name__ == "__main__":
    main(sys.argv)

