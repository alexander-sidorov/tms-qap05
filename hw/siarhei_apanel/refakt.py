from datetime import date
from typing import Any


def func(a1: float, back: float, cill: float) -> list:
    disk = back ** 2 - 4 * a1 * cill
    sqrt = disk ** 0.5
    x1 = (-back + sqrt) / 2 * a1
    x2 = (-back - sqrt) / 2 * a1
    return [x1, x2]


def far() -> None:
    4  # noqa: B018


def gar() -> int:
    return 4


def aggression(known: bool) -> str:
    if known:
        return "Оно и видно!"
    else:
        return "А могли бы и знать!"


def korteg(spisok: list) -> tuple:
    if spisok == []:
        return ()
    return (spisok[0], spisok[-1])


def newwords(words: str) -> str:
    if " " not in words:
        return words
    words1 = words.split()
    return f"{words1[1]} {words1[0]}"


def srez(spisk: Any, another: Any) -> list:
    if another not in spisk:
        return ["NoValue"]
    limit = spisk.index(another)
    return spisk[: limit + 1]  # noqa: E203


def stroki(stroka: str, stroka2: str) -> str:
    if stroka2 == "":
        return stroka
    strk = "".join(lit + stroka2 for lit in stroka if lit[-1])
    return strk[:-1]


def zaglav(stroka: str) -> str:
    if stroka == "":
        return ""
    return stroka.title()


def krypto(cod: str, key: str) -> str:
    alphavit = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(i1 if i1 == " " else alphavit[key.find(i1)] for i1 in cod)


def palindrom(di1: str) -> dict:
    result = {"errors": Any}
    if type(di1) != str:
        result["errors"] = ["TypeError"]
    else:
        i34 = 0
        j34 = len(di1) - 1
        is_palindrom = True
        while i34 < j34:
            if di1[i34] != di1[j34]:
                is_palindrom = False
            i34 += 1
            j34 -= 1
        result = {"data": True} if is_palindrom else {"data": False}
    return result


def proizvedenie(*digit: int) -> dict:

    verif = 0
    product = 1

    for dig in digit:
        result: dict[str, int] = {}

        if type(dig) in [str, tuple, list]:
            verif += 1
            if verif >= 2:
                return {"errors": ["TypeError"]}
        product *= dig

        result = {"data": product}

    return result


def dateday(yer: int, mont: int, dayz: int) -> dict:

    if (
        type(yer) in [str, tuple, list, set]
        or type(mont) in [str, tuple, list, set]  # noqa: W503
        or type(dayz) in [str, tuple, list, set]  # noqa: W503
    ):  # noqa: W503
        # noqa: W503
        return {"errors": ["TypeError"]}
    elif yer == 0 or mont <= 0 or mont > 12 or dayz <= 0 or dayz > 31:
        return {"errors": ["ValueError"]}
    else:
        result: dict[str, dict[str, int]] = {}
        data = date(yer, mont, dayz)
        now = date.today()
        delta = now - data
        result = {
            "data": {
                "year": data.year,
                "month": data.month,
                "day": data.day,
                "age": int(delta.days // 365),
            }
        }
        return result


def happybithday(yer: dict) -> dict:
    age = date(1, 1, 1)

    for keys, value in yer.items():
        if value == age:
            return {"errors": ["EqualError"]}

        if value > age:
            age = yer[keys]

    return {"data": keys}


def repeat(collect: Any) -> dict:
    noresult = []
    result = {}
    if type(collect) in [list, tuple]:
        for digit in collect:
            noresult.append(digit)
        result_dict = {
            quant: noresult.count(quant)
            for quant in noresult
            if noresult.count(quant) > 1
        }

        result["data"] = result_dict
        return result
    elif type(collect) == set:
        return {"errors": ["NoRepeatError"]}
    else:
        for value in collect.values():
            noresult.append(value)
            result_dict = {
                quant: noresult.count(quant)
                for quant in noresult
                if noresult.count(quant) > 1
            }

        result["data"] = result_dict
        return result


def html_str(query: str) -> dict:
    result: dict[str, list] = {}

    for letter in query.split("&"):
        for el in range(len(letter.split("="))):

            if letter.split("=")[el].isalpha():
                result.setdefault(letter.split("=")[el], []).append(
                    letter.split("=")[el + 1]
                )

            else:
                continue
    return {"data": result}


def decodding(code: str) -> dict:
    if type(code) != str:
        return {"errors": ["TypeError"]}
    elif len(code) % 2 != 0:
        return {"errors": ["NoQualityLetterError"]}
    else:
        return {
            "data": "".join(
                code[sym] * int(code[sym + 1])
                for sym in range(len(code))
                if code[sym].isalpha()
            )
        }


def codding(s1: str) -> dict:
    if type(s1) != str:
        return {"errors": ["TypeError"]}

    i1 = 0
    num = 0
    result = ""
    for i1 in range(len(s1)):
        j1 = i1 + 1
        if len(s1) == 1:
            result += s1[0] + "1"
            break
        if j1 == len(s1):
            t1 = s1[i1]
            if s1[-1] == s1[-2]:
                num += 1
                z1 = str(num)
            else:
                g1 = 1
                z1 = str(g1)
            result += t1 + z1
            break
        num += 1  # noqa: SIM113
        if s1[i1] != s1[j1]:
            result += s1[i1] + str(num)
            num = 0
    return {"data": result}


def rever_dict(d1: dict) -> dict:
    if type(d1) != dict:
        return {"errors": ["TypeError"]}

    result: dict[int, list] = {}
    spisok = []
    for value in d1.values():
        spisok.append(value)
    for key, value in d1.items():
        if spisok.count(value) > 1:
            result.setdefault(value, []).append(key)
        else:
            result[value] = key

    return {"data": result}


def new_dict(key: Any, value: Any) -> dict:
    result = {}
    if len(key) > len(value):
        len_none = len(key) - len(value)
        for i1 in range(len(value)):
            result[key[i1]] = value[i1]
        for j1 in range(-len_none, 0):
            result[key[j1]] = None
    elif len(key) == len(value):
        for _1 in range(len(value)):
            result[key[_1]] = value[_1]
    else:
        len_none2 = len(value) - len(key)
        for z1 in range(len(key)):
            result[key[z1]] = value[z1]
        for f1 in range(-len_none2, 0):
            result.setdefault(..., []).append(value[f1])

    return {"data": result}


def new_set(set1: set, set2: set) -> dict:
    return {
        "data": {
            "a&b": set1 & set2,
            "a|b": set1 | set2,
            "a-b": set1 - set2,
            "b-a": set2 - set1,
            "|a-b|": set1 ^ set2,
            "a in b": set1 in set2,
            "b in a": set2 in set1,
        }
    }


def diction(*digit: Any) -> dict:
    if len(digit) % 2 != 0:
        return {"errors": ["NoPares"]}
    for er in digit[::2]:
        if type(er) in [dict, set, list]:
            return {"errors": ["TypeError"]}
    result = {}
    verif = 1
    for dig in range(len(digit)):

        if dig == verif:
            verif += 2
            continue
        result[digit[dig]] = digit[dig + 1]

    return {"data": result}


if __name__ == "__main__":
    aggression(True)
