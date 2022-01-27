from collections import Counter
from collections.abc import Sequence
from datetime import date
from functools import reduce
from typing import Any
from typing import Callable
from typing import Collection


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
    return slovo == slovo[::-1]


class Palindrome01:
    def __init__(self, text: Any) -> None:
        self.__text = text

    def __bool__(self) -> Any:
        result = palindrom(self.__text)
        if "errors" in result:
            return result
        return result["data"]


@decorator_function
def umnogenie(*args: Any) -> Any:
    if len(args) < 2:
        assert isinstance(
            args[0], (Sequence, complex, int, float)
        ), "No Sequence"
        if args[0] == ("",):
            return ""
        return args[0]
    for x_1 in args:
        assert isinstance(x_1, (Sequence, complex, int, float)), "TrueError"

    return reduce(
        lambda x, y: x * y,
        args,
    )


class Multiplier04:
    def __init__(self) -> None:
        self.arg: list[Any] = []

    def add(self, arg: Any) -> Any:
        self.arg.append(arg)
        return self

    def get_result(self) -> Any:
        result = umnogenie(*self.arg)
        if "errors" in result:
            return result
        return result["data"]


@decorator_function
def date_age(b1: date) -> dict:
    assert isinstance(b1, date), "Not DateType"
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
    def __init__(self, year: Any) -> None:
        self.year = year

    @property
    def age(self) -> Any:
        result = date_age(self.year)
        if "errors" in result:
            return result
        return result["data"]["age"]


@decorator_function
def zadacha_4(day: dict[Any, date]) -> dict:

    assert isinstance(day, dict), "Is Not Dict"
    assert len(day) > 1, "Len Error"
    for value in day.values():
        assert not isinstance(value, complex)

    name = min(day, key=lambda e: day[e])
    return name


@decorator_function
def zadacha_5(collection1: Any) -> dict:
    assert isinstance(collection1, Collection), "AssertionError"
    if (
        isinstance(collection1, (set, dict, frozenset))
        and len(collection1) <= 1
    ):
        return {}

    banka = {}  # type: ignore
    list_result = []
    if len(collection1) == 0:
        return banka
    for n1 in collection1:
        list_result.append(n1)
    for n2 in list_result:
        if list_result.count(n2) > 1:
            banka[n2] = list_result.count(n2)

    return banka


class DupCounter05(Counter):
    def __init__(self, a1: Any) -> None:
        self.a1 = a1

    def get_dups(self) -> Any:
        result = zadacha_5(self.a1)
        if "errors" in result:
            return result
        return result["data"]


@decorator_function
def zadacha_7(sybol_num: Any) -> Any:
    if sybol_num == "":
        return ""
    assert isinstance(sybol_num, str), "Not String"
    assert sybol_num[0].isalpha(), "Not Digit"
    assert sybol_num[-1].isdigit(), "Not Letter"

    list_digit = []
    list_letter = []
    bank = ""

    for x1 in range(len(sybol_num)):
        if (
            sybol_num[x1].isalpha()
            and sybol_num[x1] != sybol_num[-1]
            and sybol_num[x1 + 1].isalpha()
        ):
            raise Exception("ErrorLetter")
        if sybol_num[x1].isalpha():
            list_letter.append(sybol_num[x1])
            if bank != "":
                list_digit.append(bank)
                bank = ""
        else:
            bank += sybol_num[x1]
    list_digit.append(bank)
    for x2, z1 in zip(list_letter, list_digit):
        bank += x2 * int(z1)

    return bank
