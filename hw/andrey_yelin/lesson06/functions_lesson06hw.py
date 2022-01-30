import functools
from datetime import date
from functools import wraps
from typing import Any
from typing import Collection
from typing import Counter
from typing import Dict
from urllib.parse import parse_qs

from hw.andrey_yelin.Lesson_05.yelin_lesson05 import aggression

Result = Dict[str, Any]


def decorate(func: Any) -> Any:
    @wraps(func)
    def my_decorator(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        if isinstance(result, dict) and "errors" in result:
            return result
        else:
            return {"data": result}

    return my_decorator


@decorate
def is_palindrome_1(strochka: Any = None) -> Any:
    result: Any = Any
    if strochka is None:
        result = {"errors": ["none argument"]}
        return result

    if not isinstance(strochka, str):
        result = {"errors": ["not a string"]}
        return result
    rev = "".join(reversed(strochka))

    if strochka == rev:
        result = True
    else:
        result = False
    return result


class Palindrome01:  # noqa: SIM119
    def __init__(self, word: Any) -> None:
        self.word = word

    def __bool__(self) -> Any:
        result = is_palindrome_1(self.word)
        if "errors" in result:
            return result
        return result["data"]


@decorate
def multiply_args_2(*m: Any) -> Any:
    args = [*m]

    if not len(args):
        result = {"errors": ["empty arguments"]}
        return result
    try:
        if len(args) == 1:
            args.append(1)
        multiply = functools.reduce(lambda a, b: a * b, args)
    except TypeError:
        result = {"errors": ["TypeError"]}
        return result
    result = multiply
    return result


class Multiplier04:
    def __init__(self) -> None:
        self.arg: list[Any] = []

    def add(self, arg: Any) -> Any:
        self.arg.append(arg)
        return self

    def get_result(self) -> Any:
        result = multiply_args_2(*self.arg)
        if "errors" in result:
            return result
        return result["data"]


@decorate
def age_result_3(born: Any) -> Any:
    result: Any = {}
    if not isinstance(born, date):
        result = {"errors": ["variable is not a date"]}
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
    try:
        if len(old_date) == 0:
            result = {"errors": ["empty variable"]}
            return result
        max_date = 0
        for key in old_date:
            if isinstance(old_date[key], date):
                today_time = date.today()
                ma = today_time - old_date[key]
                dd = str(ma)
                if int(dd.split()[0]) > max_date:
                    max_date = int(dd.split()[0])
                    result = key
    except TypeError:
        result = {"errors": ["TypeError"]}
    if result == {}:
        result = {"errors": ["empty variable"]}
    return result


class User02:
    def __init__(self, year: Any) -> None:
        self.year = year

    def age(self):
        result = older_4(self.year)
        if "errors" in result:
            return result
        return result["data"]["age"]


@decorate
def repeating_elements_5(elements_list: Any) -> Any:
    result: Any = {}
    zy: dict = {}
    repeat: dict = {}
    try:
        for elem in elements_list:
            if elem in zy:
                zy[elem] = zy[elem] + 1
            else:
                zy[elem] = 1
        for key in zy:
            if zy[key] > 1:
                repeat[key] = zy[key]
        else:
            result = repeat
    except TypeError:
        result = {"errors": ["TypeError"]}
    return result


class DupCounter05(Counter):
    def __init__(self, coll: Any) -> None:
        self.coll = coll

    def get_dups(self) -> Any:
        result = repeating_elements_5(self.coll)
        if "errors" in result:
            return result
        return result["data"]


@decorate
def parse_http_query_6(string: Any = None) -> Any:
    result: Any = {}
    if string is None:
        result = {"errors": ["none argument"]}
        return result
    if not isinstance(string, str):
        result = {"errors": ["variable is not a string"]}
        return result
    parse_string = parse_qs(string, keep_blank_values=True)
    if len(parse_string) == 0:
        result = {}
        return result
    result = parse_qs(string, keep_blank_values=True)
    return result


class HttpQuery03:
    def __init__(self, string: str):
        self.string = string

    def __getitem__(self, key: str) -> Any:
        try:
            parse_http_query_6(self.string)["data"][key]
        except KeyError:
            return None
        return parse_http_query_6(self.string)["data"][key]


def get_let_num_for_decode_7(command_str: str) -> tuple:  # noqa: CCR001
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
def decode_7(string: str, decode: bool = False) -> Any:
    result: Any = {}
    number: list = []
    letter: list = []

    number, letter = get_let_num_for_decode_7(string)
    if decode:
        return letter
    if len(letter) != len(number):
        result = {"errors": ["letters is not equal numbers"]}
        return result
    else:
        data = []
        for i in range(len(letter)):
            data.append(int(number[i]) * letter[i])
        result = "".join(data)
        return result


@decorate
def code_8(string: str) -> Any:  # noqa: CCR001
    result: Any = ""
    some_obj: Any = {}
    imported_string = decode_7(string, True)

    if len(imported_string["data"]) == 0:
        result = {"errors": ["number of letters = 0"]}
        return result

    lk = ""
    for index, letter in enumerate(imported_string["data"]):

        if index == 0:
            lk = letter

        if lk != letter and index != 0:
            for key in some_obj:
                result += str(key) + str(some_obj[key])
            lk = letter
            some_obj = {}
            if index == len(imported_string["data"]) - 1:
                result += str(letter) + str(1)
        elif index == len(imported_string["data"]) - 1:
            for key in some_obj:
                result += str(key) + str(some_obj[key] + 1)

        if letter in some_obj:
            some_obj[letter] += 1
        else:
            some_obj[letter] = 1

    return result


@decorate
def reversed_dictionary_9(dictionary: dict) -> dict:

    if not isinstance(dictionary, dict):
        result = {"errors": ["argument is not a dict"]}
        return result
    rev_dict = {}

    for key, value in dictionary.items():
        if value not in rev_dict:
            rev_dict[value] = [key]

        else:
            rev_dict[value].append(key)

    for some_key, some_value in rev_dict.items():
        if len(some_value) < 2:
            rev_dict[some_key] = some_value[0]
    result = rev_dict
    return result


def func_for_creating_diction(
    arg1: Any, arg2: Any, reverse: bool = False
) -> dict:
    res = {}
    for index, i in enumerate(arg1):
        if not reverse:
            res[i] = arg2[index] if len(arg2) - 1 >= index else None
        else:
            if len(arg2) - 1 < index:
                res[...] = i
            else:
                res[arg2[index]] = i
    return res


@decorate
def creating_diction_10(arg1: Any, arg2: Any) -> dict:
    result = {}

    if not arg2:
        result = {"errors": ["second argument is empty"]}
        return result
    answer = {}
    if len(arg1) >= len(arg2):
        answer = func_for_creating_diction(arg1, arg2)
    else:
        answer = func_for_creating_diction(arg2, arg1, True)

    result = answer
    return result


@decorate
def all_actions_with_two_sets_11(first_set: set, second_set: set) -> dict:

    if not isinstance(first_set, set):
        result = {"errors": ["first argument has not a set type"]}
        return result

    if not isinstance(second_set, set):
        result = {"errors": ["second argument has not a set type"]}
        return result

    return {
        "a&b": first_set & second_set,
        "a|b": first_set | second_set,
        "a-b": first_set - second_set,
        "b-a": second_set - first_set,
        "|a-b|": first_set ^ second_set,
        "a in b": first_set.issubset(second_set),
        "b in a": second_set.issubset(first_set),
    }


@decorate
def even_keys_and_odd_values_12(*args: Any) -> dict:
    if len(args) % 2 != 0:
        result = {"errors": ["quantity of arguments is not even"]}
        return result
    keys = []
    values = []
    for i in args:
        if args.index(i) % 2 == 0:
            keys.append(i)
        else:
            values.append(i)
    crafted_dict = dict(list(zip(keys, values)))
    result = crafted_dict
    return result
