from src.controllers.cryptography.cryptography import hash_passwd

def add_user(db, email, first_name, last_name, sex, birthday, passwd):
    cursor = db.cursor()

    cursor.execute("INSERT INTO user (Email, FirstName, LastName, Sex, Birthday, Password)"
                   "VALUES (%s, %s, %s, %s, %s, %s)",
                   (email, first_name, last_name, sex, birthday.strftime('%Y-%m-%d'), hash_passwd(passwd)))

    db.close()