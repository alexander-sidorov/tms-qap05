from datetime import date
from typing import Any


def palindrome(string: str) -> dict:
    result = {}
    if not isinstance(string, str):
        return {"errors": "provided argument is not a string"}
    else:
        if string[:] == string[::-1]:
            result["data"] = True
        else:
            result["data"] = False
    return result


def argum1(*args: Any) -> dict:
    result = {}
    try:
        if len(args) < 0:
            return {"errors": "no argument"}
        elif len(args) == 1:
            result["data"] = args[0]
        else:
            mresult = 1
            for i in args:
                mresult *= i
                result["data"] = mresult
    except TypeError:
        return {"errors": "given arguments' types can't be multiplied"}
    return result


def datrog(d3: Any) -> dict:
    result = {"errors": Any}
    if type(d3) != date:
        result["errors"] = ["be date"]
    else:
        s_age = {"year": d3.year, "month": d3.month, "day": d3.day, "age": int}
        today = date.today()
        age = date.today().year - d3.year

        if (d3.month > today.month) or (
            d3.month == today.month and d3.day > today.day
        ):
            age = date.today().year - d3.year - 1
        s_age["age"] = age
        result = {"date": s_age}

    return result


def ber4(birthday: dict) -> dict:
    if not isinstance(birthday, dict):  # определяет тип аргумента
        return {"errors": "Given argument is not a dictionary"}
    else:
        name_result = min(birthday, key=lambda t: birthday[t])
        return {"data": name_result}
