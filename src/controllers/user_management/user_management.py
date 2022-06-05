from src.controllers.cryptography.cryptography import hash_passwd
from src.controllers.database.database import Database

special_char = ['$', '@', '#', '%', '_', '-']


def add_user(email, first_name, last_name, sex, birthday, passwd):
    db = Database()
    cursor = db.get_cursor()
    cursor.execute("INSERT INTO user (Email, FirstName, LastName, Sex, Birthday, Password)"
                   "VALUES (%s, %s, %s, %s, %s, %s)",
                   (email, first_name, last_name, sex, birthday.strftime('%Y-%m-%d'), hash_passwd(passwd)))