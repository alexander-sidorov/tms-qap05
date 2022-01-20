import itertools
import re
import urllib.parse
from datetime import date
from itertools import groupby
from itertools import zip_longest
from typing import Any
from typing import Collection
from typing import Dict

Result = Dict[str, Any]


def decorator(func: Any) -> Any:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            result = func(*args, **kwargs)
        except AssertionError as err:
            return {"errors": [str(err)]}

        if isinstance(result, dict) and "errors" in result:
            return result

        return {"data": result}

    return wrapper


@decorator
def level_01(string: Any) -> Any:

    if not isinstance(string, str):
        raise AssertionError("argument must be string")

    else:
        if string == string[::-1]:
            result = True
        else:
            result = False

        return result


@decorator
def level_02(*arguments: Any) -> Any:

    try:
        if len(arguments) < 1:
            return {"errors": ["no arguments"]}
        elif len(arguments) == 1:
            result = arguments[0]
        else:
            pr = 1
            for i in arguments:
                pr *= i
                result = pr

    except TypeError:
        return {"errors": ["TypeError"]}

    return result


@decorator
def level_03(bd: Any) -> Any:

    today = date.today()

    if not isinstance(bd, date):
        raise AssertionError("type must be date")

    else:
        if (today.year - bd.year) < 0:
            age = None
        else:
            age = (
                today.year
                - bd.year  # noqa: W503
                - ((today.month, today.day) < (bd.month, bd.day))  # noqa: W503
            )

        result = {
            "year": bd.year,
            "month": bd.month,
            "day": bd.day,
            "age": age,
        }

    return result


@decorator
def level_04(dic: Any) -> Any:

    if not isinstance(dic, dict):
        raise AssertionError("must be date")

    else:
        try:
            res = min(dic, key=lambda n: dic[n])  # type: ignore

        except (TypeError, ValueError):
            return {"errors": ["TypeError or empty sequence"]}
        result = res

    return result


@decorator
def level_05(lis: Any) -> Any:

    if not isinstance(lis, Collection):
        raise AssertionError("argument must be list, tuple, str, set, dict")

    else:
        try:
            items = []
            for arg in lis:
                items.append(arg)
            res = {el: items.count(el) for el in items if items.count(el) > 1}
        except TypeError:
            return {"errors": ["TypeError unhashable type"]}
        result = res

    return result


@decorator
def level_06(query: Any) -> Any:

    if not isinstance(query, str):
        raise AssertionError("TypeError")

    result = urllib.parse.parse_qs(query, keep_blank_values=True)

    return result


@decorator
def level_07(string: Any) -> Any:

    if not isinstance(string, str):
        raise AssertionError(f"argument ({string=!r}) must be string")

    nums = re.findall(r"\d+", string)
    letters = re.findall(r"\D", string)
    if len(nums) != len(letters):
        return {"errors": ["wrong format of string"]}
    if not string:
        return ""
    first_el = string[0]
    if first_el.isdigit():
        return {"errors": ["wrong format of string"]}
    else:
        s1 = ["".join(g) for k, g in itertools.groupby(string, str.isalpha)]
        letter = [el for el in s1 if el.isalpha()]
        number = [int(el) for el in s1 if el.isdigit()]
        s2 = list(map(lambda s_l, s_n: s_l * s_n, letter, number))
        result = "".join(s2)

    return result


@decorator
def level_08(string: Any) -> Any:

    if not isinstance(string, str):
        raise AssertionError(f"argument ({string=!r}) must be string")

    if not string:
        return ""
    if not string.isalpha():
        return {"errors": ["argument must be without nums"]}
    else:
        col_letter = ["".join(g) for _, g in groupby(string)]
        num = []
        el = 0
        while el < len(col_letter):
            rr = len(col_letter[el])
            num.append(str(rr))
            el += 1
        letter = [x[-1] for x in col_letter]
        s1 = list(map(lambda x, y: x + y, letter, num))
        result = "".join(s1)

    return result


@decorator
def level_09(dic: Any) -> Any:
    result: Result = {}

    if not isinstance(dic, dict):
        raise AssertionError("argument must be dict")

    try:
        spisok = []
        for value in dic.values():
            spisok.append(value)
        for key, value in dic.items():
            if spisok.count(value) > 1:
                result.setdefault(value, []).append(key)
            else:
                result[value] = key
    except TypeError:
        return {"errors": ["TypeError unhashable type"]}

    return result


@decorator
def level_10(arg1: Any, arg2: Any) -> Any:

    if isinstance(arg1, (dict, set, frozenset)) or isinstance(
        arg2, (dict, set, frozenset)
    ):
        raise AssertionError("unhashable type")

    try:
        key = list(arg1)
        val = list(arg2)  # noqa: VNE002
        if len(key) >= len(val):
            result = dict(zip_longest(arg1, arg2))
        else:
            val_no_key = val[len(key) :]  # noqa: E203
            key_with_value = val[: len(key)]
            res = list(zip(key, key_with_value))
            res.append((..., val_no_key))
            result = dict(res)
        return result

    except TypeError:
        return {"errors": ["TypeError unhashable type"]}


@decorator
def level_11(s1: Any, s2: Any) -> Any:

    if not isinstance(s1, (set, frozenset)) or not isinstance(
        s2, (set, frozenset)
    ):
        raise AssertionError("arguments must be set")

    else:
        dic = {"a": s1, "b": s2}
        dic1 = dic["a"] & dic["b"]
        dic2 = dic["a"] | dic["b"]
        dic3 = dic["a"] - dic["b"]
        dic4 = dic["b"] - dic["a"]
        dic5 = dic["a"] ^ dic["b"]
        dic6 = s1.issubset(s2)
        dic7 = s2.issubset(s1)

        result = {
            "a&b": dic1,
            "a|b": dic2,
            "a-b": dic3,
            "b-a": dic4,
            "|a-b|": dic5,
            "a in b": dic6,
            "b in a": dic7,
        }

    return result


@decorator
def level_12(*arguments: Any) -> Any:

    if len(arguments) % 2 != 0:
        raise AssertionError("no pairs")

    else:
        list1 = [
            value for (key, value) in enumerate(arguments) if key % 2 == 0
        ]
        list2 = [
            value for (key, value) in enumerate(arguments) if key % 2 != 0
        ]
        try:
            list3 = dict(zip(list1, list2))
        except TypeError:
            return {"errors": ["TypeError"]}

        result = list3

    return result
