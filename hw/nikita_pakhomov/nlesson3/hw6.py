from datetime import date
from typing import Any
from typing import Dict

type_1 = Dict[str, Any]


def is_palindrome(text: str) -> type_1:
    result = {}
    if type(text) == str:
        if text[::-1] == text:
            result["data"] = True
        else:
            result["data"] = False
    else:
        result["errors"] = False
    return result


def level_2(*args: Any) -> dict:
    result = {}

    if args == 0:
        result["errors"] = 0
    else:
        nakopitel = 1
        for i in args:
            nakopitel *= i

        result["data"] = nakopitel
    return result


def level_3(born: Any) -> dict:
    result = {}

    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, month=born.month + 1, day=1)
    if birthday > today:
        age = today.year - born.year - 1
        result["data"] = {
            "year": born.year,
            "month": born.month,
            "day": born.day,
            "age": age,
        }
        age = today.year - born.year - 1
        return result
    else:
        age = today.year - born.year
        result["data"] = {
            "year": born.year,
            "month": born.month,
            "day": born.day,
            "age": age,
        }
        return result


def level_4(age: Any) -> dict:
    result = {}
    if type(age) == dict:
        a_peremen = age["A"]
        b_peremen = age["B"]
        if type(age["A"]) != date or type(age["B"]) != date:
            result["errors"] = "this is not a date"
            return result
        elif a_peremen > b_peremen:
            result["data"] = "B"
            return result
        elif age["A"] < age["B"]:
            result["data"] = "A"
            return result
        elif age["A"] == age["B"]:
            result["errors"] = "dates are equal"
            return result
        else:
            result["errors"] = "dates are equal"
            return result

    else:
        result["errors"] = "this is not a date"
        return result


def level_5(spisok: Any) -> dict:
    result: dict = {}
    clovar: dict = {}
    for iii in spisok:
        if iii in clovar:
            clovar[iii] = clovar[iii] + 1
        else:
            clovar[iii] = 1
    for yyy in spisok:
        if clovar[yyy] <= 1:
            del clovar[yyy]
    result["data"] = clovar
    return result
