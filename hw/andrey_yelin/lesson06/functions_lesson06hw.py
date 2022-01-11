import functools
from datetime import date
from typing import Any
from urllib.parse import parse_qs


def is_palindrome_1(strochka: Any = None) -> dict:
    result = {}
    if strochka is None:
        result["errors"] = "none argument"
        return result
    if not isinstance(strochka, str):
        result["errors"] = "not a string"
        return result
    rev = "".join(reversed(strochka))

    if strochka == rev:
        result["data"] = True  # type: ignore
    else:
        result["data"] = False  # type: ignore
    return result


def multiply_args_2(*m: Any) -> dict:
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


def age_result_3(born: Any) -> dict:
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


def older_4(old_date: Any) -> dict:
    result = {}
    if len(old_date) == 0:
        result["errors"] = "empty variable"
        return result
    max_date = 0

    for key in old_date:
        today_time = date.today()
        ma = today_time - old_date[key]
        dd = str(ma)
        if int(dd.split()[0]) > max_date:
            max_date = int(dd.split()[0])
            result["data"] = key
    return result


def repeating_elements_5(elements_list: Any) -> dict:
    result: dict = {}
    zy: dict = {}
    repeat: dict = {}
    for elem in elements_list:
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
        result["data"] = repeat
    return result


def parse_http_query_6(string: Any = None) -> dict:
    result = {}
    if string is None:
        result["errors"] = "none argument"
        return result
    if not isinstance(string, str):
        result["errors"] = "variable is not a string"
        return result
    parse_string = parse_qs(string)
    if len(parse_string) == 0:
        result["errors"] = "empty string"
        return result
    result = {"data": parse_qs(string)}  # type: ignore
    return result


def decode_7(string: Any = None) -> dict:  # noqa: CCR001
    result = {}
    if string is None:
        result["errors"] = "none argument"
        return result
    number = []
    letter = []
    symb = ""
    if len(string) < 2:
        result["errors"] = "so short string"
        return result
    index = 0
    for sym in list(string):
        try:
            isinstance(float(sym), float)
            symb = symb + sym
            if index == (len(list(string)) - 1):
                number.append(float(symb))
        except BaseException:
            letter.append(sym)
            if symb != "":
                number.append(float(symb))
            symb = ""
        index += 1  # noqa: SIM113
    if len(letter) != len(number):
        result["errors"] = "letters not equal to numbers"
        return result
    else:
        data = []
        for i in range(len(letter)):
            data.append(int(number[i]) * letter[i])
        result["data"] = "".join(data)
        return result
