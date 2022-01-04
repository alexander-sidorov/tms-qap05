import functools
from datetime import date


def isPalindrome(s=None):
    result = {}
    if s is None:
        result["errors"] = "none argument"
        return result
    if not isinstance(s, str):
        result["errors"] = "not a string"
        return result
    rev = "".join(reversed(s))

    if s == rev:
        result["data"] = True
    else:
        result["data"] = False
    return result


def multiplyArgs(*m):
    result = {}
    args = [*m]
    if not len(args):
        result["errors"] = "empty argument"
        return result
    for i in args:
        if not isinstance(i, int):
            result["errors"] = "variable is not integer"
            return result
    multiply = functools.reduce(lambda a, b: a * b, args)
    result["data"] = multiply
    return result


def ageResult(born):
    result = {}
    if not isinstance(born, date):
        result["errors"] = "variable is not date"
        return result
    today = date.today()
    age = int(
        today.year
        - born.year
        - ((today.month, today.day) < (born.month, born.day))
    )
    result["data"] = {
        "year": born.year,
        "month": born.month,
        "day": born.day,
        "age": age,
    }
    return result
