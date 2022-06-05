from src.controllers.cryptography.cryptography import hash_passwd
from src.controllers.database.database import Database
import datetime


def add_user(user):
    db = Database()
    cursor = db.get_cursor()
    cursor.execute("INSERT INTO user (Email, FirstName, LastName, Sex, Birthday, Password)"
                   "VALUES (%s, %s, %s, %s, %s, %s)",
                   (user.get_email(), user.get_first_name(), user.get_last_name(), user.get_sex(),
                    datetime.datetime.strptime(user.get_birthday().replace(".", "-"), '%d-%m-%y'), hash_passwd(user.get_passwd())))
    db.get_database().close()
