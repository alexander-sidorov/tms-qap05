from typing import Any
from typing import Dict
from datetime import date

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
    if not isinstance(born, date):
        result["errors"] = "variable is not a date"
        return result
    today = date.today()
    age = int(
        today.year
        - born.year  # noqa: W503
        - ((today.month, today.day) < (born.month, born.day))  # noqa: W503
    )
    result["data"] = {  # type: ignore
        "year": born.year,
        "month": born.month,
        "day": born.day,
        "age": age,
    }
    return result
