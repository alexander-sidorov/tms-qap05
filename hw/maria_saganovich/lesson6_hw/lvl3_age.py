from datetime import date
from typing import Any


def func3_age(d1: Any) -> dict:
    result = {"errors": Any}
    if type(d1) != date:
        result["errors"] = ["should be date"]
    else:
        some_age = {
            "year": d1.year,
            "month": d1.month,
            "day": d1.day,
            "age": int,
        }
        today = date.today()
        age = date.today().year - d1.year

        if d1.month > today.month:
            age = date.today().year - d1.year - 1
        elif d1.month == today.month:
            if d1.day > today.day:
                age = date.today().year - d1.year - 1
        some_age["age"] = age
        result = {"data": some_age}

    return result
