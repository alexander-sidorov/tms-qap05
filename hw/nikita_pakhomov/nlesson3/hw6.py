from datetime import date
from typing import Any
from typing import Dict

type_1 = Dict[str, Any]


def decorate(func: Any) -> Any:
    def xxx(*args: Any) -> Any:
        result = func(*args)
        if isinstance(result, dict) and "errors" in result:
            return result

        return {"data": result}

    return xxx


@decorate
def is_palindrome(text: str) -> type_1:
    result = {}
    if type(text) == str:
        if text[::-1] == text:
            result = True
        else:
            result = False
    else:
        result = False
    return result


@decorate
def level_2(*args: Any) -> dict:
    result = {}

    nakopitel = 1
    for i in args:
        nakopitel *= i

    result = nakopitel
    return result


@decorate
def level_3(born: Any) -> dict:
    result = {}

    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, month=born.month + 1, day=1)
    if birthday > today:
        age = today.year - born.year - 1
        result = {
            "year": born.year,
            "month": born.month,
            "day": born.day,
            "age": age,
        }
        return result
    else:
        age = today.year - born.year
        result = {
            "year": born.year,
            "month": born.month,
            "day": born.day,
            "age": age,
        }
        return result


@decorate
def level_4(age: Any) -> dict:
    result = {}
    if type(age) == dict:
        a_peremen = age["A"]
        b_peremen = age["B"]
        if type(age["A"]) != date or type(age["B"]) != date:
            result["errors"] = "invalid input"
            return result
        elif a_peremen > b_peremen:
            result = "B"
            return result
        elif age["A"] < age["B"]:
            result = "A"
            return result

        else:
            result["errors"] = "invalid input"
            return result
    else:
        result["errors"] = "invalid input"
        return result


@decorate
def level_4_1(age: Dict[Any, date]) -> dict:
    result = {}
    if type(age) == dict:
        if type(age["A"]) != date or type(age["B"]) != date:
            result["errors"] = "this is not a date"

        name = min(age, key=lambda n: age[n])
        return name
    else:
        result["errors"] = "dates are equal"
        return result


@decorate
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
    result = clovar
    return result
