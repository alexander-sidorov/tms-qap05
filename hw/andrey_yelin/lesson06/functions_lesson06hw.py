import functools
from datetime import date
from typing import Any
from typing import Dict
from urllib.parse import parse_qs

Result = Dict[str, Any]


def is_palindrome_1(strochka: Any = None) -> dict:
    result: Dict[str, Any] = {}
    if strochka is None:
        result["errors"] = "none argument"
        return result
    if not isinstance(strochka, str):
        result["errors"] = "not a string"
        return result
    rev = "".join(reversed(strochka))

    if strochka == rev:
        result["data"] = True
    else:
        result["data"] = False
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
    result: Dict[str, Any] = {}
    if not isinstance(born, date):
        result["errors"] = "variable is not a date"
        return result
    today = date.today()
    age = int(
        today.year
        - born.year  # noqa: W503
        - ((today.month, today.day) < (born.month, born.day))  # noqa: W503
    )
    result["data"] = {
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


def older_4_v_lambda(old_date: Dict[Any, date]) -> Result:
    result: Result = {}
    if not old_date:
        result["errors"] = "empty variable"
        return result

    res = min(old_date, key=lambda n: old_date[n])
    result["data"] = res

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
    result: Dict[str, Any] = {}
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
    result = {"data": parse_qs(string)}
    return result


def decode_7(string: str) -> dict:
    result, number, letter, symbl, index = {}, [], [], "", 0
    for sym in string:
        try:
            isinstance(int(sym), int)
            symbl = symbl + sym
            if index == (len(string) - 1):
                number.append(int(symbl))
        except BaseException:
            letter.append(sym)
            if symbl != "":
                number.append(int(symbl))
            symbl = ""
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
