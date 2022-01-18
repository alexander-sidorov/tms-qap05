from datetime import date
from typing import Any
from typing import Callable


def decorator_function(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        solution = func(*args, **kwargs)
        if isinstance(solution, dict) and "errors" in solution:
            return solution
        return {"data": solution}

    return wrapper


@decorator_function
def palindrom(slovo: Any) -> Any:
    if type(slovo) != str:
        return {"errors": ["TypeErrors"]}

    once_letter = 0
    last_letter = len(slovo) - 1
    palindrom = True

    while once_letter < last_letter:
        if slovo[once_letter] != slovo[last_letter]:
            palindrom = False
        once_letter += 1
        last_letter -= 1

    return palindrom


@decorator_function
def umnogenie(*nums: Any) -> Any:
    count1 = 0
    banka = 1
    for n2 in nums:
        if type(n2) in [str, tuple, list]:
            count1 += 1
            if count1 >= 2:
                return {"errors": ["TypeError"]}
        banka *= n2
    return banka


@decorator_function
def date_age(b1: date) -> dict:
    if type(b1) != date:
        return {"errors": ["TypeError"]}
    segodnya = date.today()
    delta = segodnya - b1
    result = {
        "year": b1.year,
        "month": b1.month,
        "day": b1.day,
        "age": int(delta.days // 365),
    }
    return result


@decorator_function
def zadacha_4(day: dict[Any, date]) -> dict:

    if isinstance(day, dict) is False:
        return {"errors": ["TypeError"]}
    if len(day) < 1:
        return {"errors": ["NonValueError"]}
    for value in day.values():
        if isinstance(value, complex):
            return {"errors": ["TypeError"]}

    name = min(day, key=lambda e: day[e])
    return name


@decorator_function
def zadacha_5(collection: Any) -> dict:
    if type(collection) in [set, dict]:
        return {}
    if type(collection) not in [list, tuple, str]:
        return {"errors": ["TypeError"]}

    banka = {}  # type: ignore
    list_result = []
    if len(collection) == 0:
        return banka
    for n1 in collection:
        if collection.count(n1) >= 2:
            list_result.append(n1)
    for n2 in list_result:
        if type(n2) in [list, dict]:
            return {"errors": ["TypeError"]}
        else:
            banka[n2] = list_result.count(n2)

    return banka


@decorator_function
def zadacha_7(sybol_num: Any) -> Any:
    if len(sybol_num) == 0:
        return ""
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

    return bank2
