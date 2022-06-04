import re
from src.controllers.cryptography.cryptography import hash_passwd
from src.controllers.database.database import Database

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
special_char = ['$', '@', '#', '%', '_', '-']


def add_user(email, first_name, last_name, sex, birthday, passwd):
    db = Database()
    cursor = db.get_cursor()
    cursor.execute("INSERT INTO user (Email, FirstName, LastName, Sex, Birthday, Password)"
                   "VALUES (%s, %s, %s, %s, %s, %s)",
                   (email, first_name, last_name, sex, birthday.strftime('%Y-%m-%d'), hash_passwd(passwd)))


def validate_email(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def validate_passwd(passwd):
    # Password needs to be >= 8 characters
    if len(passwd) < 12:
        return False

    # Password needs to contain at least 1 digit
    if not any(char.isdigit() for char in passwd):
        return False

    # Password needs to contain at least 1 uppercase letter
    if not any(char.isupper() for char in passwd):
        return False

    # Password needs to contain at least 1 lowercase letter
    if not any(char.islower() for char in passwd):
        return False

    if not any(char in special_char for char in passwd):
        return False

    return True
