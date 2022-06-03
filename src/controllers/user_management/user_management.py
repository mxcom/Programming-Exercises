import re
from src.controllers.cryptography.cryptography import hash_passwd

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
special_char = ['$', '@', '#', '%', '_', '-']


def add_user(db, email, first_name, last_name, sex, birthday, passwd):
    cursor = db.cursor()

    cursor.execute("INSERT INTO user (Email, FirstName, LastName, Sex, Birthday, Password)"
                   "VALUES (%s, %s, %s, %s, %s, %s)",
                   (email, first_name, last_name, sex, birthday.strftime('%Y-%m-%d'), hash_passwd(passwd)))

    db.close()


def validate_email(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def validate_passwd(passwd):
    # Password needs to be >= 8 characterss
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
