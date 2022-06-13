import math
from datetime import date

from src.controllers.user_management.user_management import *


def calc_kcal(sex, height, weight, birthday):

    current_date = date.today() - birthday

    age = math.floor(current_date.days / 365)

    if sex == 'female':
        return int((10 * weight) + (6.25 * height) + (5 * age) - 161)
    else:
        return int((10 * weight) + (6.25 * height) + (5 * age) + 5)



