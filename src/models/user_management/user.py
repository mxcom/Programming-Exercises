from datetime import datetime


class User:
    def __init__(self, email, first_name, last_name, sex, birthday, height, weight, passwd):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.birthday = birthday
        self.height = height
        self.weight = weight
        self.passwd = passwd

    def get_email(self):
        return self.email

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_sex(self):
        return self.sex

    def get_birthday(self):
        return self.birthday

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_passwd(self):
        return self.passwd

    def set_email(self, email):
        self.email = email

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_sex(self, sex):
        self.sex = sex

    def set_birthday(self, birthday):
        if type(birthday) is datetime:
            self.birthday = birthday

    def set_height(self, height):
        self.height = height

    def set_weight(self, weight):
        self.weight = weight

    def set_passwd(self, passwd):
        self.passwd = passwd
