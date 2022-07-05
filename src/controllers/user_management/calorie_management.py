import datetime
import random

from src.controllers.database.database import Database
from src.controllers.user_management.calc_kcal import calc_kcal
from src.controllers.primary.daily_track import DailyTrack
from PySide6.QtCharts import QBarSet
import random


def get_daily_calories(user):
    try:
        date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM calories WHERE Date LIKE %s AND UserID LIKE %s;",
                       (date, user.get_id()))

        for i in cursor.fetchall():
            return i[3]

        calories = calc_kcal(user.get_sex(), user.get_height(), user.get_weight(), user.get_birthday())
        cursor.execute("INSERT INTO calories (UserID, Calories, CaloriesEaten, Date)"
                       "VALUES (%s, %s, %s, %s);",
                       (user.get_id(), calories, 0, date))
        db.get_database().close()
    except Exception as e:
        print(e)


def update_calories(user, old_calories, new_calories):
    try:
        date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        db = Database()
        cursor = db.get_cursor()
        total = old_calories + new_calories
        cursor.execute("UPDATE calories SET CaloriesEaten = %s WHERE Date LIKE %s AND UserID LIKE %s ",
                       (total, date, user.get_id()))

        return total
    except Exception as e:
        print(e)


def add_dummy_kcal():
    try:
        db = Database()
        cursor = db.get_cursor()
        date = datetime.datetime.now()
        for i in range(100):
            date = date - datetime.timedelta(1)
            cursor.execute("INSERT INTO calories (UserID, Calories, CaloriesEaten, Date)  "
                           "VALUES (55, 2085, %s, %s)", (random.randint(1800, 2300), date.strftime("%Y-%m-%d")))
    except Exception as e:
        print(e)


def add_dummy_bp():
    try:
        db = Database()
        cursor = db.get_cursor()
        date = datetime.datetime.now()
        for i in range(100):
            date = date - datetime.timedelta(1)
            cursor.execute("INSERT INTO bloodpressure (UserID, Diastolic, Systolic, Date)  "
                           "VALUES (55, %s, %s, %s)", (random.randint(65, 80), random.randint(115, 125), date.strftime("%Y-%m-%d")))
    except Exception as e:
        print(e)


def add_dummy_steps():
    try:
        db = Database()
        cursor = db.get_cursor()
        date = datetime.datetime.now()
        for i in range(100):
            date = date - datetime.timedelta(1)
            cursor.execute("INSERT INTO steps (UserID, Steps, Date)  "
                           "VALUES (55, %s, %s)", (random.randint(2500, 15000), date.strftime("%Y-%m-%d")))
    except Exception as e:
        print(e)


def add_dummy_weight():
    try:
        db = Database()
        cursor = db.get_cursor()
        date = datetime.datetime.now()
        for i in range(100):
            date = date - datetime.timedelta(1)
            cursor.execute("INSERT INTO weight (UserID, Grams, Date)  "
                           "VALUES (55, %s, %s)", (random.randint(80, 85), date.strftime("%Y-%m-%d")))
    except Exception as e:
        print(e)