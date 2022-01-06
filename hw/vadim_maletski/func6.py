from collections import Counter
from datetime import date
from itertools import zip_longest
from typing import Any


def level_01(string: Any) -> dict:
    result = {}
    errors = []

    if not string:
        errors.append("argument must not be empty")
    if type(string) == int:
        errors.append("argument must not be number")
    if errors:
        result["errors"] = errors

    else:
        if string == string[::-1]:
            result["data"] = True  # type: ignore
        else:
            result["data"] = False  # type: ignore

    return result


def level_02(arguments: Any) -> dict:
    result = {}
    errors = []

    data = len(str(arguments))

    if not arguments:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        if data == 1:
            result["data"] = int(arguments)  # type: ignore

        else:
            ans = 1
            for i in arguments:
                ans *= i

            result["data"] = ans  # type: ignore

    return result


def level_03(bd: Any) -> dict:
    result = {}
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

        result["data"] = {  # type: ignore
            "year": bd.year,
            "month": bd.month,
            "day": bd.day,
            "age": age,
        }

    return result


def level_04(dic: Any) -> dict:
    result = {}
    errors = []

    if dic["A"] == dic["B"]:
        errors.append("years must be a different")
    if errors:
        result["errors"] = errors

    else:
        if dic["A"] > dic["B"]:
            result["data"] = "B"  # type: ignore
        else:
            result["data"] = "A"  # type: ignore

    return result


def level_05(lis: Any) -> dict:
    result = {}
    errors = []

    if not lis:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        res = dict(  # noqa: C402
            (x, lis.count(x)) for x in set(lis) if lis.count(x) > 1
        )  # noqa: C402

        result["data"] = res  # type: ignore

    return result


def level_06(query: Any) -> dict:
    result = {}
    errors = []

    if not query:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        query2 = query.replace("=", "")
        query3 = query2.split("&")

        num = len(query3)
        res1 = []
        i = 0
        while i < num:
            res1.append(tuple(query3[i]))
            i += 1

        res2 = {}  # type: ignore
        for key, value in res1:
            res2.setdefault(key, list())  # noqa: C408
            res2[key].append(value)

            result["data"] = res2  # type: ignore

    return result


def level_07(string: Any) -> dict:
    result = {}
    errors = []

    if not string:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        s1 = list(string[::2])
        s2 = list(string[1::2])

        s3 = [k * int(v) for (k, v) in zip(s1, s2)]
        s4 = "".join(s3)

        result["data"] = s4  # type: ignore

    return result


def level_08(string: Any) -> dict:
    result = {}
    errors = []

    if not string:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        s1 = list(string[::])
        dic = Counter(s1)
        s2 = (f"{key}{value}" for (key, value) in dic.items())
        s3 = "".join(s2)

        result["data"] = s3  # type: ignore

    return result


def level_09(dic: Any) -> dict:
    result = {}
    errors = []

    if not dic:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        lis = [(value, key) for key, value in dic.items()]

        res = {}  # type: ignore
        for key, value in lis:
            res.setdefault(key, list())  # noqa: C408
            res[key].append(value)

            result["data"] = res  # type: ignore

    return result


def level_10a(a1: Any, b1: Any) -> dict:
    result = {}
    errors = []

    if not a1:
        errors.append("argument must not be empty")
    if not b1:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        a11 = list(a1)
        d1 = dict(zip_longest(a11, b1))

        result["data"] = d1  # type: ignore
    return result


def level_10b(a2: Any, b2: Any) -> dict:
    result = {}
    errors = []

    if not a2:
        errors.append("argument must not be empty")
    if not b2:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        a22 = list(a2)
        d2 = dict(zip_longest(a22, b2, fillvalue="..."))
        result["data"] = d2  # type: ignore

    return result


def level_11(s1: Any, s2: Any) -> dict:
    result = {}
    errors = []

    if not s1:
        errors.append("argument must not be empty")
    if not s2:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        dic = {"a": s1, "b": s2}
        dic1 = dic["a"] & dic["b"]
        dic2 = dic["a"] | dic["b"]
        dic3 = dic["a"] - dic["b"]
        dic4 = dic["b"] - dic["a"]
        dic5 = dic["a"] ^ dic["b"]
        dic6 = dic["a"] in dic["b"]
        dic7 = dic["b"] in dic["a"]

        result["data"] = {  # type: ignore
            "a&b": dic1,
            "a|b": dic2,
            "a-b": dic3,
            "b-a": dic4,
            "|a-b|": dic5,
            "a in b": dic6,
            "b in a": dic7,
        }

    return result


def level_12(arg: Any) -> dict:
    result = {}
    errors = []

    if not arg:
        errors.append("argument must not be empty")
    if errors:
        result["errors"] = errors

    else:
        list1 = [value for (key, value) in enumerate(arg) if key % 2 == 0]
        list2 = [value for (key, value) in enumerate(arg) if key % 2 != 0]

        list3 = dict(zip(list1, list2))

        result["data"] = list3  # type: ignore

    return result
