import functools
from datetime import date
from typing import Any


def isPalindrome(s: Any = None) -> dict:  # noqa: N802, VNE001
    result = {}
    if s is None:
        result["errors"] = "none argument"
        return result
    if not isinstance(s, str):
        result["errors"] = "not a string"
        return result
    rev = "".join(reversed(s))

    if s == rev:
        result["data"] = True  # type: ignore
    else:
        result["data"] = False  # type: ignore
    return result


def multiplyArgs(*m: Any) -> dict:  # noqa: N802
    result = {}
    args = [*m]
    if not len(args):
        result["errors"] = "empty arguments"
        return result
    for i in args:
        if not isinstance(i, int) and not isinstance(i, float):
            result["errors"] = "variable is not a number"
            return result
    multiply = functools.reduce(lambda a, b: a * b, args)
    result["data"] = multiply
    return result


def ageResult(born: Any) -> dict:  # noqa: N802
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


def older(oldDate: Any) -> dict:  # noqa: N803
    result = {}
    if len(oldDate) == 0:
        result["errors"] = "empty variable"
        return result
    maxDate = 0  # noqa: N806

    for key in oldDate:
        t = date.today()  # noqa: VNE001
        ma = t - oldDate[key]
        dd = str(ma)
        if int(dd.split()[0]) > maxDate:
            maxDate = int(dd.split()[0])  # noqa: N806
            result["data"] = key
    return result


def repeatingElements(elementsList: Any) -> dict:  # noqa: N802, N803
    result = {}
    zy = {}  # type: ignore
    repeat = {}
    for elem in elementsList:
        if elem in zy:
            zy[elem] = zy[elem] + 1
        else:
            zy[elem] = 1
    for key in zy:
        if zy[key] > 1:
            repeat[key] = zy[key]
    if len(repeat) == 0:
        result["data"] = "elements are not repeat"
        return result
    else:
        result["data"] = repeat  # type: ignore
    return result
