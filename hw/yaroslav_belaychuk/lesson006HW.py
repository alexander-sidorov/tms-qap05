from datetime import date
from typing import Any


def palindrom(slovo: str) -> dict:
    if type(slovo) != str:
        return {"errors": ["TypeErrors"]}
    else:
        once_letter = 0
        last_letter = len(slovo) - 1
        palindrom = True
    while once_letter < last_letter:
        if slovo[once_letter] != slovo[last_letter]:
            palindrom = False
        once_letter += 1
        last_letter -= 1
    result = {"data": True} if palindrom else {"data": False}
    return result


def umnogenie(*nums: Any) -> dict:
    banka = 1
    for n2 in nums:
        banka *= n2
    return {"data": banka}


def date_age(b1: date) -> dict:
    if type(b1) != date:
        return {"TypeError"}  # type: ignore

    segodnya = date.today()
    delta = segodnya - b1
    result = {
        "data": {
            "year": b1.year,
            "month": b1.month,
            "day": b1.day,
            "age": int(delta.days // 365),
        }
    }
    return result


def zadacha_4(day: dict) -> dict:
    keys = []
    values = []
    for key, value in day.items():
        keys.append(key)
        values.append(value)

    name = keys[values.index(min(values))]
    return {"data": name}


def zadacha_5(collection: Any) -> dict:
    if type(collection) not in [list, tuple, str]:
        return {"errors": ["NoRepeatError"]}
    banka = {}
    if len(collection) == 0:
        return {"error"}  # type: ignore
    for n1 in collection:
        if collection.count(n1) >= 2:
            banka[n1] = collection.count(n1)
    return {"data": banka}


def zadacha_7(sybol_num: str) -> dict:
    if type(sybol_num) != str:
        return {"TypeError"}  # type: ignore
    if len(sybol_num) % 2 != 0:
        return {"Error"}  # type: ignore
    banka = ""
    b3 = tuple(filter(str.isalpha, sybol_num))
    c3 = tuple(filter(str.isdigit, sybol_num))
    for x1, z1 in zip(b3, c3):
        banka += x1 * int(z1)
    return {"data": banka}
