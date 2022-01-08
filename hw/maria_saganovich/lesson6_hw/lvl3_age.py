from datetime import date
from typing import Any


def func3_age(d: Any) -> dict:
    result = {"errors": Any}
    if type(d) != date:
        result["errors"] = ["should be date"]
    else:
        some_age = {"year": d.year, "month": d.month, "day": d.day, "age": int}
        today = date.today()
        age = date.today().year - d.year

        if d.month > today.month:
            age = date.today().year - d.year - 1
        elif d.month == today.month:
            if d.day > today.day:
                age = date.today().year - d.year - 1
        some_age["age"] = age
        result = {"data": some_age}

    return result
