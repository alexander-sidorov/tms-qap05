import functools
from datetime import date
from typing import Any
from typing import Callable
from typing import Dict
from urllib.parse import parse_qs
from functools import wraps

Result = Dict[str, Any]


def decorate(func: Callable) -> Callable:
    @wraps(func)
    def my_decorator(*args: Any, **kwargs: Any) -> Any:
        try:
            return {"data": func(*args, **kwargs)}
        except Exception as f:
            return {"errors": [str(f)]}

    return my_decorator


@decorate
def is_palindrome_1(strochka: Any = None) -> Any:
    result: Any = 0
    if strochka is None:
        result = "none argument"
        return result
    if not isinstance(strochka, str):
        result = "not a string"
        return result
    rev = "".join(reversed(strochka))

    if strochka == rev:
        result = True
    else:
        result = False
    return result


@decorate
def multiply_args_2(*m: Any) -> Any:
    result: Any = {}
    args = [*m]
    if not len(args):
        result = "empty arguments"
        return result
    for i in args:
        if not isinstance(i, int) and not isinstance(i, float):
            result = "variable is not a number"
            return result
    multiply = functools.reduce(lambda a, b: a * b, args)
    result = multiply
    return result


@decorate
def age_result_3(born: Any) -> Any:
    result: Any = {}
    if not isinstance(born, date):
        result = "variable is not a date"
        return result
    today = date.today()
    age = int(
        today.year
        - born.year  # noqa: W503
        - ((today.month, today.day) < (born.month, born.day))  # noqa: W503
    )
    result = {
        "year": born.year,
        "month": born.month,
        "day": born.day,
        "age": age,
    }
    return result


@decorate
def older_4(old_date: Any) -> Any:
    result: Any = {}
    if len(old_date) == 0:
        result = "empty variable"
        return result
    max_date = 0
    for key in old_date:
        today_time = date.today()
        ma = today_time - old_date[key]
        dd = str(ma)
        if int(dd.split()[0]) > max_date:
            max_date = int(dd.split()[0])
            result = key
    return result


def older_4_v_lambda(old_date: Dict[Any, date]) -> Result:
    result: Result = {}
    if not old_date:
        result["errors"] = "empty variable"
        return result

    res = min(old_date, key=lambda n: old_date[n])
    result["data"] = res

    return result


@decorate
def repeating_elements_5(elements_list: Any) -> Any:
    result: Any = {}
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
        result = "elements are not repeat"
        return result
    else:
        result = repeat
    return result


@decorate
def parse_http_query_6(string: Any = None) -> Any:
    result: Any = {}
    if string is None:
        result = "none argument"
        return result
    if not isinstance(string, str):
        result = "variable is not a string"
        return result
    parse_string = parse_qs(string)
    if len(parse_string) == 0:
        result = "empty string"
        return result
    result = parse_qs(string)
    return result


def get_let_num_for_decode_7(command_str: str) -> tuple:
    index, number, letter, symbl = 0, [], [], ""
    for sym in command_str:
        try:
            isinstance(int(sym), int)
            symbl = symbl + sym
            if index == (len(command_str) - 1):
                number.append(int(symbl))
        except BaseException:
            letter.append(sym)
            if symbl != "":
                number.append(int(symbl))
            symbl = ""
        index += 1  # noqa: SIM113
    return number, letter


@decorate
def decode_7(string: str) -> Any:
    result, number, letter, = (
        {},
        [],
        [],
    )

    number, letter = get_let_num_for_decode_7(string)
    if len(letter) != len(number):
        result = "letters not equal to numbers"
        return result
    else:
        data = []
        for i in range(len(letter)):
            data.append(int(number[i]) * letter[i])
        result = "".join(data)
        return result
