import datetime
from src.controllers.database.database import Database
from src.controllers.user_management.calc_kcal import calc_kcal
from PySide6.QtCharts import QBarSet


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
        return 0
    except Exception as e:
        print(e)


def update_calories(user, old_calories, new_calories):
    try:
        date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        db = Database()
        cursor = db.get_cursor()
        total = old_calories + new_calories
        cursor.execute("UPDATE calories SET CaloriesEaten = %s WHERE Date LIKE %s AND UserID LIKE %s",
                       (total, date, user.get_id()))

        return total
    except Exception as e:
        print(e)


def get_stat_kcal(user, period):
    try:
        db = Database()
        cursor = db.get_cursor()
        if period == 1:
            cursor.execute("SELECT CaloriesEaten FROM calories WHERE UserID LIKE %s AND "
                           "Date BETWEEN  DATE_SUB(now(), INTERVAL 1 WEEK) AND now();",
                           (user.get_id(),))
        elif period == 2:
            cursor.execute(
                "SELECT CaloriesEaten FROM calories WHERE MONTH(now() - INTERVAL 1 MONTH) AND UserID LIKE %s",
                (user.get_id(),))
        elif period == 3:
            cursor.execute("SELECT CaloriesEaten FROM calories WHERE UserID LIKE %s ORDER BY Date",
                           (user.get_id(),))
        else:
            return None

        results = []
        for i in cursor.fetchall():
            results.append(i[0])

        # results = QBarSet("kcal")
        # for i in cursor.fetchall():
        #    results << i[0]

        return results
    except Exception as e:
        print(e)


def get_stat_steps(user, period):
    try:
        db = Database()
        cursor = db.get_cursor()
        if period == 1:
            cursor.execute("SELECT CaloriesEaten FROM calories WHERE UserID LIKE %s AND "
                           "Date BETWEEN  DATE_SUB(now(), INTERVAL 1 WEEK) AND now();",
                           (user.get_id(),))
        elif period == 2:
            cursor.execute(
                "SELECT CaloriesEaten FROM calories WHERE MONTH(now() - INTERVAL 1 MONTH) AND UserID LIKE %s",
                (user.get_id(),))
        elif period == 3:
            cursor.execute("SELECT CaloriesEaten FROM calories WHERE UserID LIKE %s ORDER BY Date",
                           (user.get_id(),))
        else:
            return None

        results = []
        for i in cursor.fetchall():
            results.append(i[0])

        return results
    except Exception as e:
        print(e)
