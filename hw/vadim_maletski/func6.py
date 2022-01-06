from collections import Counter
from datetime import date
from itertools import zip_longest


def level_01(string: str) -> dict:  # type: ignore
    result = {}

    if type(string) != str:
        result["error"] = f"Wrong input type ({string}) -, need string"

    else:
        if string == string[::-1]:
            result["data"] = True  # type: ignore

        else:
            result["data"] = False  # type: ignore

    return result


def level_02(arguments: tuple) -> dict:
    data = len(str(arguments))
    result = {}

    if arguments == "":
        result["error"] = "No arguments"
    elif type(arguments) == str:
        result["error"] = f"({arguments}) Must be list of numbers"

    else:
        if data == 1:
            result["data"] = arguments  # type: ignore

        else:
            ans = 1
            for i in arguments:
                ans *= i

                result["data"] = ans  # type: ignore

    return result


def level_03(bd: date) -> dict:
    today = date.today()
    result = {}

    if bd.year <= today.year:
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

    else:
        result["error"] = "Incorrect year"  # type: ignore

    return result


def level_04(dic: dict) -> dict:
    result = {}

    if dic["A"] == dic["B"]:
        result["error"] = "Years must be a different"

    elif dic["A"] > dic["B"]:
        result["data"] = "B"

    else:
        result["data"] = "A"

    return result


def level_05(lis: list) -> dict:
    result = {}

    if type(lis) != list:
        result["error"] = f"({lis}) Must be list"

    elif not lis:
        result["error"] = f"({lis}) List is empty"

    else:
        res = dict(  # noqa: C402
            (x, lis.count(x)) for x in set(lis) if lis.count(x) > 1
        )

        result["data"] = res  # type: ignore

    return result


def level_06(query: str) -> dict:
    result = {}

    if type(query) != str:
        result["error"] = f"({query}) Must be string"

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


def level_07(string: str) -> dict:
    result = {}

    if type(string) != str:
        result["error"] = f"({string}) Must be string"
    else:

        s1 = list(string[::2])
        s2 = list(string[1::2])

        s3 = [k * int(v) for (k, v) in zip(s1, s2)]
        s4 = "".join(s3)

        result["data"] = s4

    return result


def level_08(string: str) -> dict:
    result = {}

    if type(string) != str:
        result["error"] = f"({string}) Must be string"

    else:
        s1 = list(string[::])
        dic = Counter(s1)
        s2 = (f"{key}{value}" for (key, value) in dic.items())
        s3 = "".join(s2)

        result["data"] = s3

    return result


def level_09(dic: dict) -> dict:
    result = {}

    if type(dic) != dict:
        result["error"] = f"({dic}) Must be dict"

    else:
        lis = [(value, key) for key, value in dic.items()]

        res = {}  # type: ignore
        for key, value in lis:
            res.setdefault(key, list())  # noqa: C408
            res[key].append(value)

            result["data"] = res  # type: ignore

    return result


def level_10a(a1: str, b1: list) -> dict:
    result = {}

    if type(a1) != str:
        result["error"] = f"({a1}) Must be string"
    elif type(b1) != list:
        result["error"] = f"({b1}) Must be list"
    elif type(b1) == str:
        result["error"] = f"({b1}) Must be list of numbers"

    else:
        a11 = list(a1)
        d1 = dict(zip_longest(a11, b1))

        result["data"] = d1  # type: ignore
    return result


def level_10b(a2: str, b2: list) -> dict:
    result = {}
    if type(a2) != str:
        result["error"] = f"({a2}) Must be string"
    elif type(b2) != list:
        result["error"] = f"({b2}) Must be list"
    elif type(b2) == str:
        result["error"] = f"({b2}) Must be list of numbers"

    else:
        a22 = list(a2)
        d2 = dict(zip_longest(a22, b2, fillvalue="..."))
        result["data"] = d2  # type: ignore

    return result


def level_11(s1: set, s2: set) -> dict:
    result = {}

    if type(s1) != set:
        result["error"] = f"({s1}) Must be set"
    elif type(s2) != set:
        result["error"] = f"({s2}) Must be set"

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


def level_12(arg: tuple) -> dict:
    result = {}

    if arg == "":
        result["error"] = "No arguments"
    elif type(arg) == str:
        result["error"] = f"({arg}) Must be list of numbers"

    else:
        list1 = [
            value for (key, value) in enumerate(arg) if key % 2 == 0
        ]  # noqa: E501  # type: ignore
        list2 = [
            value for (key, value) in enumerate(arg) if key % 2 != 0
        ]  # noqa: E501  # type: ignore

        list3 = dict(zip(list1, list2))

        result["data"] = list3  # type: ignore

    return result
