from datetime import datetime


class User:

    def __init__(self, id='', email='', first_name='', last_name='', sex='', birthday='', height='', weight='', passwd=''):
        self._id = id
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._sex = sex
        self._birthday = birthday
        self._height = height
        self._weight = weight
        self._passwd = passwd

    def get_id(self):
        return self._id

    def get_email(self):
        return self._email

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_sex(self):
        return self._sex

    def get_birthday(self):
        return self._birthday

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weight

    def get_passwd(self):
        return self._passwd

    def set_id(self, id):
        self._id = id

    def set_email(self, email):
        self._email = email

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_sex(self, sex):
        self._sex = sex

    def set_birthday(self, birthday):
        self._birthday = birthday

    def set_height(self, height):
        self._height = int(height)

    def set_weight(self, weight):
        self._weight = int(weight)

    def set_passwd(self, passwd):
        self._passwd = passwd
