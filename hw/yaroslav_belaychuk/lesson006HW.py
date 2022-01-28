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
    return min(day, key=lambda e: day[e])


@decorator_function
def zadacha_5(collection1: Any) -> dict
    assert isinstance(collection1, Collection), "AssertionError"
    if (
        isinstance(collection1, (set, dict, frozenset))
        and len(collection1) <= 1  # noqa: W503
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
    assert isinstance(sybol_num, str), "Not String"
    if sybol_num == "":
        return ""
    assert sybol_num[-1].isdigit(), "Not Digit"
    assert sybol_num[0].isalpha(), "Not Letter"

    list_digit = []
    list_letter = []
    bank = ""

    for x1 in range(len(sybol_num)):
        if (
            sybol_num[x1].isalpha()
            and sybol_num[x1] != sybol_num[-1]  # noqa: W503
            and sybol_num[x1 + 1].isalpha()  # noqa: W503
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

    return "".join(x2 * int(z1) for x2, z1 in zip(list_letter, list_digit))


@decorator_function
def zadacha_6(query: Any) -> dict:
    assert isinstance(query, str), "Not String"
    if len(query) < 2:
        return {}
    if "=" not in query:
        return {query: [""]}
    result: dict[str, list] = {}
    for letter in query.split("&"):
        verif = letter.index("=")
        new_letter = letter[:verif]
        if new_letter not in result:
            result[new_letter] = [letter[verif + 1 :]]  # noqa: E203
        else:
            result[new_letter].append(letter[verif + 1 :])  # noqa: E203

    return result


class HttpQuery03:
    def __init__(self, string_text: Any) -> None:
        self.string_text = string_text
        self.dict_empty: dict[Any, Any] = {}

    def __getitem__(self, item: Any) -> Any:
        self.dict_empty = zadacha_6(self.string_text)
        if "errors" in self.dict_empty:
            return self.dict_empty
        if (
            isinstance(self.dict_empty["data"].get(item), list)
            and len(self.dict_empty["data"].get(item)) == 1  # noqa: W503
        ):
            return self.dict_empty["data"].get(item)[0]
        return self.dict_empty["data"].get(item)
