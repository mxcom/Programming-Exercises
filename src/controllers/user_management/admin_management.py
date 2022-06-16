import datetime
from src.controllers.cryptography.cryptography import hash_passwd, compare_passwd
from src.controllers.database.database import Database
from src.models.user_management.admin import Admin

def get_admin(identifier):
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM admin WHERE Identification LIKE %s",
                       (identifier, ))

        admin = Admin()
        for i in cursor.fetchall():
            admin.set_admin_id(i[0])
            admin.set_identifier(i[1])
            admin.set_password(i[2])

        return admin
    except Exception as e:
        print(e)
        return None

def change_user_info(user_id):
    try:
        print("asdf")
    except Exception as e:
        print(e)




