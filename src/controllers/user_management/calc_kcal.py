from datetime import date

from src.controllers.user_management.user_management import *


def calc_kcal(sex, height, weight, birthday):

    current_date = date.today()
    age = current_date - birthday
    print(age)

    if sex == 'female':
        return (10 * weight) + (6, 25 * height) + (5 * age) - 161
    else:
        return (10 * weight) + (6, 25 * height) + (5 * age) + 5



