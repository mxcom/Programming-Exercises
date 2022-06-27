import datetime
from src.controllers.database.database import Database
from src.controllers.user_management.calc_kcal import calc_kcal
from PySide6.QtCharts import QBarSet


def get_stat_kcal(user, period):
    try:
        db = Database()
        cursor = db.get_cursor()
        if period == 1:
            cursor.execute("SELECT CaloriesEaten FROM calories WHERE UserID LIKE %s and Date > now() - INTERVAL 1 week",
                           (user.get_id(),))
        elif period == 2:
            cursor.execute(
                "SELECT CaloriesEaten FROM calories WHERE UserID LIKE %s AND Date > now() - INTERVAL 1 month;",
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
            cursor.execute("SELECT Steps FROM steps WHERE UserID LIKE %s and Date > now() - INTERVAL 1 week;",
                           (user.get_id(),))
        elif period == 2:
            cursor.execute(
                "SELECT Steps FROM steps WHERE UserID LIKE %s and Date > now() - INTERVAL 1 month;",
                (user.get_id(),))
        elif period == 3:
            cursor.execute("SELECT Steps FROM steps WHERE UserID LIKE %s ORDER BY Date",
                           (user.get_id(),))
        else:
            return None

        results = []
        for i in cursor.fetchall():
            results.append(i[0])

        return results
    except Exception as e:
        print(e)


def get_stat_sys(user, period):
    try:
        db = Database()
        cursor = db.get_cursor()
        if period == 1:
            cursor.execute("SELECT Systolic FROM bloodpressure WHERE UserID LIKE %s AND Date > now() - INTERVAL 1 week;",
                           (user.get_id(),))
        elif period == 2:
            cursor.execute(
                "SELECT Systolic FROM bloodpressure WHERE UserID LIKE %s AND Date > now() - INTERVAL 1 month;",
                (user.get_id(),))
        elif period == 3:
            cursor.execute("SELECT Systolic FROM bloodpressure WHERE UserID LIKE %s ORDER BY Date",
                           (user.get_id(),))

        results = []
        for i in cursor.fetchall():
            results.append(i[0])

        return results
    except Exception as e:
        print(e)


def get_stat_dia(user, period):
    try:
        db = Database()
        cursor = db.get_cursor()
        if period == 1:
            cursor.execute("SELECT Diastolic FROM bloodpressure WHERE UserID LIKE %s AND Date > now() - INTERVAL 1 week;",
                           (user.get_id(),))
        elif period == 2:
            cursor.execute(
                "SELECT Diastolic FROM bloodpressure WHERE UserID LIKE %s AND Date > now() - INTERVAL 1 month;",
                (user.get_id(),))
        elif period == 3:
            cursor.execute("SELECT Diastolic FROM bloodpressure WHERE UserID LIKE %s ORDER BY Date",
                           (user.get_id(),))

        results = []
        for i in cursor.fetchall():
            results.append(i[0])

        return results
    except Exception as e:
        print(e)

def get_stat_weight(user, period):
    try:
        db = Database()
        cursor = db.get_cursor()
        if period == 1:
            cursor.execute("SELECT Grams FROM weight WHERE UserID LIKE %s AND Date > now() - INTERVAL 1 week;",
                           (user.get_id(),))
        elif period == 2:
            cursor.execute(
                "SELECT Grams FROM weight WHERE UserID LIKE %s AND Date > now() - INTERVAL 1 month;",
                (user.get_id(),))
        elif period == 3:
            cursor.execute("SELECT Grams FROM weight WHERE UserID LIKE %s ORDER BY Date",
                           (user.get_id(),))

        results = []
        for i in cursor.fetchall():
            results.append(i[0])

        return results
    except Exception as e:
        print(e)