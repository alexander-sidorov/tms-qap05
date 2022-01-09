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

    if not arguments:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        pr = 1
        for i in arguments:
            pr *= i
            result["data"] = pr

    return result


def level_03(bd: Any) -> Result:
    result: Result = {}
    errors = []

    today = date.today()

    if bd.year > today.year:
        errors.append("wrong year")
    if errors:
        result["errors"] = errors

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


def level_04(dic: dict[str, date]) -> Result:
    result: Result = {}
    errors = []

    if dic["A"] == dic["B"]:
        errors.append("years must be a different")
    if errors:
        result["errors"] = errors

    else:
        if dic["A"] > dic["B"]:
            result["data"] = "B"
        else:
            result["data"] = "A"

    return result


def level_05(lis: Any) -> Result:
    result: Result = {}
    errors = []

    if type(lis) == bool:
        errors.append("argument must not be bool")
    if errors:
        result["errors"] = errors

    else:
        if type(lis) == set:
            res = {}  # type: ignore
            result["data"] = res

        else:
            res = {(x, lis.count(x)) for x in lis if lis.count(x) > 1}  # type: ignore
            result["data"] = dict(res)

    return result


def level_06(query: Any) -> Result:
    result: Result = {}
    errors = []

    if type(query) == int:
        errors.append(f"argument ({query=!r}) must be string")
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
        for _ in enumerate(dic):
            rr = len(dic[el])
            res.append(rr)
            el += 1  # noqa: SIM113

        s2 = {key: value for (key, value) in zip(dic, res)}
        s2 = (f"{key}{value}" for (key, value) in s2.items())  # type: ignore
        s3 = "".join(s2)
        s4 = "".join(c[0] for c in itertools.groupby(s3))

        result["data"] = s4

    return result


def level_09(dic: Any) -> Result:
    result: Result = {}
    errors = []

    if not dic:
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


def level_10(a1: Any, b1: Any, a2: Any, b2: Any) -> Result:
    result: Result = {}
    errors = []

    if not a1:
        errors.append(f"arguments ({a1=!r}) must not be empty")
    if not b1:
        errors.append(f"arguments ({b1=!r}) must not be empty")
    if not a2:
        errors.append(f"arguments ({a2=!r}) must not be empty")
    if not b2:
        errors.append(f"arguments ({b2=!r}) must not be empty")
    if errors:
        result["errors"] = errors

    else:
        a11 = list(a1)
        d1 = dict(zip_longest(a11, b1))

        a22 = list(a2)
        d2 = dict(zip_longest(a22, b2, fillvalue="..."))

        result["data"] = d1, d2

    return result


def level_11(s1: Any, s2: Any) -> Result:
    result: Result = {}
    errors = []

    if type(s1) == str:
        errors.append(f"argument {s1=!r} must be set")
    if type(s2) == str:
        errors.append(f"argument {s2=!r} must be set")
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


def level_12(arg: Any) -> Result:
    result: Result = {}
    errors = []

    if not arg:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        list1 = [value for (key, value) in enumerate(arg) if key % 2 == 0]
        list2 = [value for (key, value) in enumerate(arg) if key % 2 != 0]

        list3 = dict(zip(list1, list2))

        result["data"] = list3

    return result
