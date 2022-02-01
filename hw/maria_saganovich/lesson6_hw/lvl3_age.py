import datetime
from datetime import date
from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func3_age(d1: Any) -> dict:
    assert isinstance(d1, (datetime.date, datetime.datetime)), [
        "should be date"
    ]

    today = date.today()
    age = date.today().year - d1.year

    if (d1.month > today.month) or (
        d1.month == today.month and d1.day > today.day
    ):
        age = date.today().year - d1.year - 1

    return {
        "year": d1.year,
        "month": d1.month,
        "day": d1.day,
        "age": age,
    }
