from datetime import date
from typing import Any


def decorat(func: Any) -> Any:
    def wrapper(*args1: Any, **kw: Any) -> Any:
        result = func(*args1, **kw)
        if isinstance(result, dict) and "errors" in result:
            return result
        return {"data": result}

    return wrapper


@decorat
def palindrome(string: str) -> Any:
    result = {}
    if not isinstance(string, str):
        return {"errors": "provided argument is not a string"}
    else:
        if string[:] == string[::-1]:
            result = True
        else:
            result = False
    return result


@decorat
def argum1(*args: Any) -> Any:
    result = 0
    try:
        if len(args) < 1:
            return {"errors": ["no argument"]}
        elif len(args) == 1:
            result = args[0]
        else:
            mresult = 1
            for i in args:
                mresult *= i
                result = mresult
    except TypeError:
        return {"errors": ["given arguments' types can't be multiplied"]}
    return result


@decorat
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


@decorat
def ber4(birthday: dict[Any, date]) -> Any:
    if not isinstance(birthday, dict):  # определяет тип аргумента
        return {"errors": ["not a dictionary"]}
    else:
        name_result = min(birthday, key=lambda t: birthday[t])
        return {"data": name_result}
