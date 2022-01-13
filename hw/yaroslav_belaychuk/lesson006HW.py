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
    count1 = 0
    banka = 1
    for n2 in nums:
        if type(n2) in [str, tuple, list]:
            count1 += 1
            if count1 >= 2:
                return {"errors": ["TypeError"]}
        banka *= n2
    return {"data": banka}


def date_age(b1: date) -> dict:
    if type(b1) != date:
        return {"errors": ["TypeError"]}
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
    if type(day) != dict:
        return {"errors": ["TypeError"]}
    if len(day) < 1:
        return {"errors": ["NonValueError"]}
    keys = []
    values = []
    for key, value in day.items():
        if type(value) != date:
            return {"errors": ["TypeError"]}
        keys.append(key)
        values.append(value)
    name = keys[values.index(min(values))]
    return {"data": name}


def zadacha_5(collection: Any) -> dict:
    if type(collection) in [set, dict]:
        return {"data": {}}
    if type(collection) not in [list, tuple, str]:
        return {"errors": ["TypeError"]}
    banka = {}
    list_result = []
    if len(collection) == 0:
        return {"data": banka}
    for n1 in collection:
        if collection.count(n1) >= 2:
            list_result.append(n1)
    for n2 in list_result:
        if type(n2) in [list, dict]:
            return {"errors": ["TypeError"]}
        else:
            banka[n2] = list_result.count(n2)
    return {"data": banka}


print(zadacha_5([]))


def zadacha_7(sybol_num: str) -> dict:
    if len(sybol_num) == 0:
        return {"data": ""}
    if type(sybol_num) != str:
        return {"errors": ["TypeError"]}
    if sybol_num[-1].isalpha():
        return {"errors": ["NonDigitError"]}
    if sybol_num[0].isdigit():
        return {"errors": ["NonLetterError"]}
    list_digit = []
    list_letter = []
    bank = ""
    bank2 = ""
    for x1 in sybol_num:
        if x1.isalpha():
            list_letter.append(x1)
            if bank != "":
                list_digit.append(bank)
                bank = ""
        else:
            bank += x1
    list_digit.append(bank)
    for x1, z1 in zip(list_letter, list_digit):
        bank2 += x1 * int(z1)

    return {"data": bank2}
