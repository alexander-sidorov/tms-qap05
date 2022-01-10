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
    for n in nums:
        banka *= n
    return {"data": banka}


def date_age(b: date) -> dict:
    if type(b) != date:
        return {"TypeError"}

    segodnya = date.today()
    delta = segodnya - b
    result = {
        "data": {
            "year": b.year,
            "month": b.month,
            "day": b.day,
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
        return {"error"}
    for n in collection:
        if collection.count(n) >= 2:
            banka[n] = collection.count(n)
    return {"data": banka}


def zadacha_7(sybol_num: str) -> dict:
    if type(sybol_num) != str:
        return {"TypeError"}
    if len(sybol_num) % 2 != 0:
        return {"Error"}
    banka = ""
    b = tuple(filter(str.isalpha, sybol_num))
    c = tuple(filter(str.isdigit, sybol_num))
    for x, z in zip(b, c):
        banka += x * int(z)
    return {"data": banka}
