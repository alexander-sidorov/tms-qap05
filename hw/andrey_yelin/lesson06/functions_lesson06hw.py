import functools
from datetime import date
from datetime import datetime


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


def older(oldDate):
    result = {}
    if len(oldDate) == 0:
        result["errors"] = "empty variable"
        return result
    maxDate = 0

    for key in oldDate:
        t = date.today()
        ma = t - oldDate[key]
        dd = str(ma)
        if int(dd.split()[0]) > maxDate:
            maxDate = int(dd.split()[0])
            result["data"] = key
    return result


c = [(), "", "", 1, 1]


def repeatingElements(elementsList):
    result = {}
    zy = {}
    repeat = {}
    for elem in elementsList:
        if elem in zy:
            zy[elem] = zy[elem] + 1
        else:
            zy[elem] = 1
    print(zy)
    for key in zy:
        if zy[key] > 1:
            repeat[key] = zy[key]
    if len(repeat) == 0:
        result["data"] = "elements are not repeat"
        return result
    else:
        result["data"] = repeat
    return result
