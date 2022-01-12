from datetime import date
from typing import Any


def palindrom(string: str) -> dict:
    result = {}
    if not isinstance(string, str):
        return {"errors": ["Is not string type"]}
    if string[:] == string[::-1]:
        result["data"] = True
    else:
        result["data"] = False
    return result


def factorial(*numbers: Any) -> dict:
    result: Any = 1
    for number in numbers:
        if not isinstance(number, (int, float, complex, str, list, tuple)):
            return {"errors": ["Unsupported type"]}

        if isinstance(result, (list, str)) and isinstance(
            number, (list, tuple, str)
        ):
            return {"errors": ["Can't multiply sequence by non-int of types"]}

        result *= number

    return {"data": result}


def age(d1: Any) -> dict:
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
        if (today.month < d1.month) or (
            (today.month == d1.month) and (today.day < d1.day)
        ):
            age = date.today().year - d1.year - 1
            some_age["age"] = age
            result = {"data": some_age}

        return result


def older(d1: Any) -> dict:
    age = date(1, 1, 1)

    for keys, value in d1.items():
        if value == age:
            return {"errors": ["EqualError"]}

        if value > age:
            age = d1[keys]

    return {"data": keys}
