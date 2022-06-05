from src.controllers.cryptography.cryptography import hash_passwd, compare_passwd
from src.controllers.database.database import Database
import datetime


def add_user(user):
    db = Database()
    cursor = db.get_cursor()
    cursor.execute("INSERT INTO user (Email, FirstName, LastName, Sex, Birthday, Height, Password)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (user.get_email(), user.get_first_name(), user.get_last_name(), user.get_sex(),
                    datetime.datetime.strptime(user.get_birthday().replace(".", "-"), '%d-%m-%y'), int(user.get_height()),
                    hash_passwd(user.get_passwd())))
    db.get_database().close()


def search_user(email):
    db = Database()
    cursor = db.get_cursor()
    try:
        cursor.execute("SELECT Email, Password FROM user WHERE Email LIKE %s", (email,))
        data = cursor.fetchall()

        for i in data:
            if i[0] == email:
                return True
            else:
                return False
    except Exception as e:
        print(e)
        return False


def validate_user(email, passwd):
    db = Database()
    cursor = db.get_cursor()
    try:
        cursor.execute("SELECT Email, Password FROM user WHERE Email LIKE %s", (email,))
        data = cursor.fetchall()

        for i in data:
            if compare_passwd(passwd, i[1]):
                return True
            else:
                return False
    except Exception as e:
        print(e)
        return False

