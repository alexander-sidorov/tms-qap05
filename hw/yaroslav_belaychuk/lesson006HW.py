from datetime import date
from typing import Any
from typing import Callable
from collections.abc import Sequence
from functools import reduce

def decorator_function(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            solution = func(*args, **kwargs)
            return {"data": solution}
        except Exception as f1:
            return {"errors": [str(f1)]}

    return wrapper




@decorator_function
def palindrom(slovo: Any) -> Any:
    assert isinstance(slovo, str), "Not string"
    return slovo == slovo[:: -1]

class Palindrome01:
    def __init__(self, text):
        self.__text = text
    def __bool__(self):
        return palindrom(self.__text)




@decorator_function
def umnogenie(*args: Any) -> Any:
    if len(args) < 2:
        assert isinstance(args[0], (Sequence, complex, int, float)), "No Sequence"
        if args[0] == ("",):
            return ""
        return args[0]
    for _1 in args:
        assert isinstance(_1, (Sequence, complex, int, float)), "TrueError"

    return reduce(
        lambda x, y: x * y,
        args,
    )


@decorator_function
def date_age(b1: date) -> dict:
 #   assert not isinstance(b1, date), "Not DateType"
    segodnya = date.today()
    delta = segodnya - b1
    result = {
        "year": b1.year,
        "month": b1.month,
        "day": b1.day,
        "age": int(delta.days // 365),
    }
    return result

class User02:
    def __init__(self, year):
        self.year = year
    def age(self):
        return date_age(self.year)["data"]["age"]
d = User02(date(2020, 1, 23))







@decorator_function
def zadacha_4(day: dict[Any, date]) -> dict:

    assert isinstance(day, dict), "Is Not Dict"
    assert len(day) > 1, "Len Error"
    for value in day.values():
        assert not isinstance(value, complex)

    name = min(day, key=lambda e: day[e])
    return name


@decorator_function
def zadacha_5(collection: Any) -> dict:
    if isinstance(collection, (set, dict)):
        return {}
    assert isinstance(collection, (list, tuple, str)), "TypeError"

    banka = {}  # type: ignore
    list_result = []
    if len(collection) == 0:
        return banka
    for n1 in collection:
        if collection.count(n1) >= 2:
            list_result.append(n1)
    for n2 in list_result:
        assert not isinstance(n2, (list, dict))
        banka[n2] = list_result.count(n2)

    return banka

class Counter:


class DupCounter05(Counter):
    def __init__(self, a1):
        self.a1 = a1
    def get_dubs(self):
        return zadacha_7(self.a1)


@decorator_function
def zadacha_7(sybol_num: Any) -> Any:
    if len(sybol_num) == 0:
        return ""
    assert isinstance(sybol_num, str), "Not String"
    assert not sybol_num[-1].isalpha(), "Not Digit"
    assert not sybol_num[0].isdigit(), "Not Letter"

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
