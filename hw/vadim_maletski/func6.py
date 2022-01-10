import itertools
from datetime import date
from itertools import groupby
from itertools import zip_longest
from typing import Any
from typing import Dict
from urllib.parse import parse_qs

Result = Dict[str, Any]


def level_01(string: Any) -> Result:
    result: Result = {}
    errors = []

    if type(string) != str:
        errors.append("argument must be string")
    if errors:
        result["errors"] = errors

    else:
        if string == string[::-1]:
            result["data"] = True
        else:
            result["data"] = False

    return result


def level_02(*arguments: Any) -> Result:
    result: Result = {}
    errors = []

    try:
        if not arguments:
            errors.append("argument must not be empty")

        if errors:
            result["errors"] = errors

        else:
            pr = 1
            for i in arguments:
                pr *= i
                result["data"] = pr

    except TypeError:
        return {"errors": f"types {arguments=!r} must be not multiplied"}

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


def level_04(dic: Any) -> Result:
    result: Result = {}
    errors = []

    if type(dic) != dict:
        errors.append("argument must be dict")
    if errors:
        result["errors"] = errors

    else:
        res = min(dic, key=dic.get)
        result["data"] = res

    return result


def level_05(lis: Any) -> Result:
    result: Result = {}
    errors = []

    try:
        if not isinstance(lis, (dict, list, str, tuple)):
            errors.append("argument must be collection")
        if errors:
            result["errors"] = errors

        else:
            res = {(x, lis.count(x)) for x in lis if lis.count(x) > 1}
            result["data"] = dict(res)

    except TypeError:
        return {"errors": "unhashable type"}

    return result


def level_06(query: Any) -> Result:
    result: Result = {}
    errors = []

    if not isinstance(query, str):
        errors.append("argument must be string")
    if errors:
        result["errors"] = errors

    else:
        res = parse_qs(query)

        result["data"] = res

    return result


def level_07(string: Any) -> Result:
    result: Result = {}
    errors = []

    if type(string) != str:
        errors.append(f"argument ({string=!r}) must be string")
    if errors:
        result["errors"] = errors

    else:
        letter = [el for el in string if not el.isdigit()]

        num_list = []
        num = ""
        for char in string:
            if char.isdigit():
                num = num + char
            else:
                if num != "":
                    num_list.append(int(num))
                    num = ""
        if num != "":
            num_list.append(int(num))

            s3 = [k * v for (k, v) in zip(list(num_list), list(letter))]
            s4 = "".join(s3)

            result["data"] = s4

    return result


def level_08(string: Any) -> Result:
    result: Result = {}
    errors = []

    if type(string) != str:
        errors.append(f"argument ({string=!r}) must be string")
    if errors:
        result["errors"] = errors

    else:
        dic = ["".join(g) for _, g in groupby(string)]

        res = []

        el = 0
        while el < len(dic):
            rr = len(dic[el])
            res.append(rr)
            el += 1

        s2 = {key: value for (key, value) in zip(dic, res)}
        s3 = "".join("".join((str(k), str(v))) for k, v in s2.items())
        s4 = "".join(map("".join, tuple(s3)))
        s5 = "".join(c[0] for c in itertools.groupby(s4))

        result["data"] = s5

    return result


def level_09(dic: Any) -> Result:
    result: Result = {}
    errors = []

    if not isinstance(dic, dict):
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        res = {
            n: [key for key in dic.keys() if dic[key] == n]
            for n in set(dic.values())
        }

        result["data"] = res

    return result


def level_10(args1: Any, args2: Any) -> Result:
    result: Result = {}
    errors = []

    if not isinstance(args1, (list, str, tuple)):
        errors.append("argument must be list, str or tuple")
    if not isinstance(args2, (list, str, tuple)):
        errors.append("argument must be list, str or tuple")
    if errors:
        result["errors"] = errors

    else:
        if len(args1) > len(args2):
            args11 = list(args1)
            dic = dict(zip_longest(args11, args2))
        else:
            args22 = list(args1)
            dic = dict(zip_longest(args22, args2, fillvalue="..."))

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
    errors = []

    if not arguments:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        list1 = [
            value for (key, value) in enumerate(arguments) if key % 2 == 0
        ]
        list2 = [
            value for (key, value) in enumerate(arguments) if key % 2 != 0
        ]

        list3 = dict(zip(list1, list2))

        result["data"] = list3

    return result
