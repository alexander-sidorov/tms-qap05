import itertools
import re
from datetime import date
from itertools import groupby
from itertools import zip_longest
from typing import Any
from typing import Dict

Result = Dict[str, Any]


def level_01(string: Any) -> Result:
    result: Result = {}

    if type(string) != str:
        return {"errors": ["argument must be string"]}

    else:
        if string == string[::-1]:
            result["data"] = True
        else:
            result["data"] = False

    return result


def level_02(*arguments: Any) -> Result:
    result: Result = {}

    try:
        if len(arguments) < 1:
            return {"errors": ["no arguments"]}

        elif len(arguments) == 1:
            result["data"] = arguments[0]

        else:
            pr = 1
            for i in arguments:
                pr *= i
                result["data"] = pr
    except TypeError:
        return {"errors": ["TypeError"]}

    return result


def level_03(bd: Any) -> Result:
    result: Result = {}
    errors = []

    today = date.today()

    if not isinstance(bd, date):
        errors.append("type must be date")
    if errors:
        result["errors"] = errors

    else:
        if (today.year - bd.year) < 0:
            age = None
            result["data"] = age
        else:
            age = (
                today.year
                - bd.year  # noqa: W503
                - ((today.month, today.day) < (bd.month, bd.day))  # noqa: W503
            )

        result["data"] = {
            "year": bd.year,
            "month": bd.month,
            "day": bd.day,
            "age": age,
        }

    return result


def level_04(dic: dict[Any, date]) -> Result:
    result: Result = {}
    errors = []

    if type(dic) != dict:
        errors.append("argument must be date")
    if errors:
        result["errors"] = errors

    else:
        try:
            res = min(dic, key=lambda n: dic[n])

        except TypeError:
            return {"errors": ["TypeError"]}

        result["data"] = res

    return result


def level_05(lis: Any) -> Result:
    result: Result = {}

    if type(lis) not in [list, tuple, str, set, dict]:
        return {"errors": ["argument must be list, tuple, str, set, dict"]}

    else:
        try:
            items = []
            for arg in lis:
                items.append(arg)
            res = {el: items.count(el) for el in items if items.count(el) > 1}
        except TypeError:
            return {"errors": ["TypeError unhashable type"]}
        result["data"] = res

    return result


def level_06(query: Any) -> Result:
    result: Result = {}
    if not isinstance(query, str):
        return {"errors": ["TypeError"]}
    lis2 = query.split("&")
    for lis in lis2:
        for el in range(len(lis.split("="))):
            if lis.split("=")[el] != lis.split("=")[-1]:
                result.setdefault(lis.split("=")[el], []).append(
                    lis.split("=")[el + 1]
                )
    return {"data": result}


def level_07(string: Any) -> Result:

    if not isinstance(string, str):
        return {"errors": [f"argument ({string=!r}) must be string"]}
    nums = re.findall(r"\d+", string)
    letters = re.findall(r"\D", string)
    if len(nums) != len(letters):
        return {"errors": ["wrong format of string"]}
    if not string:
        return {"data": ""}
    first_el = string[0]
    if first_el.isdigit():
        return {"errors": ["wrong format of string"]}
    else:
        s1 = ["".join(g) for k, g in itertools.groupby(string, str.isalpha)]
        letter = [el for el in s1 if el.isalpha()]
        number = [int(el) for el in s1 if el.isdigit()]
        s2 = list(map(lambda s_l, s_n: s_l * s_n, letter, number))
        return {"data": "".join(s2)}


def level_08(string: Any) -> Result:
    result: Result = {}

    if type(string) != str:
        return {"errors": [f"argument ({string=!r}) must be string"]}
    if not string:
        return {"data": ""}
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
        s2 = "".join(s1)

        result["data"] = s2

    return result


def level_09(dic: Any) -> Result:
    result: Result = {}

    if not isinstance(dic, dict):
        return {"errors": ["argument must be dict"]}
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

    return {"data": result}


def level_10(arg1: Any, arg2: Any) -> Result:
    result: Result = {}

    if type(arg1) not in (list, str, tuple):
        return {"errors": ["unhashable type"]}

    else:
        if any((isinstance(arg1, (list, set, dict)) for el in arg1)):
            return {"errors": ["unhashable type"]}
        key = list(arg1)
        val = list(arg2)  # noqa: VNE002
        if len(key) >= len(val):
            dic = dict(zip_longest(key, val))
            result["data"] = dic
        else:
            val_no_key = val[len(key) :]  # noqa: E203
            key_with_value = val[: len(key)]
            res = list(zip(key, key_with_value))
            res.append((..., val_no_key))
            dic = dict(res)
            result["data"] = dic

    return result


def level_11(s1: Any, s2: Any) -> Result:
    result: Result = {}
    errors = []

    if not isinstance(s1, (set, frozenset)):
        errors.append("argument must be set")
    if not isinstance(s2, (set, frozenset)):
        errors.append("argument must be set")
    if errors:
        result["errors"] = errors

    else:
        dic = {"a": s1, "b": s2}
        dic1 = dic["a"] & dic["b"]
        dic2 = dic["a"] | dic["b"]
        dic3 = dic["a"] - dic["b"]
        dic4 = dic["b"] - dic["a"]
        dic5 = dic["a"] ^ dic["b"]
        dic6 = s1.issubset(s2)
        dic7 = s2.issubset(s1)

        result["data"] = {
            "a&b": dic1,
            "a|b": dic2,
            "a-b": dic3,
            "b-a": dic4,
            "|a-b|": dic5,
            "a in b": dic6,
            "b in a": dic7,
        }

    return result


def level_12(*arguments: Any) -> Result:
    result: Result = {}

    if len(arguments) % 2 != 0:
        return {"errors": ["no pairs"]}

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

        result["data"] = list3

    return result
