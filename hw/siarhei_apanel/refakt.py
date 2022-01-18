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


def srez(spisk: list, another: int) -> list:
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


def decor_data(func: Any) -> Any:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        if isinstance(result, dict) and "errors" in result:
            return result
        return {"data": result}

    return wrapper


@decor_data
def palindrom(di1: Any) -> Any:
    if type(di1) != str:
        return {"errors": ["TypeError"]}
    i34 = 0
    j34 = len(di1) - 1
    is_palindrom = True
    while i34 < j34:
        if di1[i34] != di1[j34]:
            is_palindrom = False
        i34 += 1
        j34 -= 1
    return is_palindrom


@decor_data
def proizvedenie(*digit: Any) -> Any:

    verif = 0
    product = 1

    for dig in digit:

        if type(dig) in [str, tuple, list]:
            verif += 1
            if verif >= 2:
                return {"errors": ["TypeError"]}
        product *= dig

    return product


@decor_data
def dateday(yer: Any) -> Any:

    if type(yer) != date:
        return {"errors": ["TypeError"]}

    now = date.today()
    delta = now - yer

    return {
        "year": yer.year,
        "month": yer.month,
        "day": yer.day,
        "age": int(delta.days // 365),
    }


@decor_data
def happybithday(yer: dict[Any, date]) -> Any:
    if isinstance(yer, dict) is False:
        return {"errors": ["TypeError"]}

    return min(yer, key=lambda t: yer[t])


@decor_data
def repeat(collect: Any) -> dict:
    if type(collect) not in [list, tuple, str] or len(collect) < 2:
        return {"errors": ["NoRepeatError"]}
    noresult = []
    for digit in collect:
        noresult.append(digit)
    return {
        quant: noresult.count(quant)
        for quant in noresult
        if noresult.count(quant) > 1
    }


@decor_data
def html_str(query: Any) -> dict:
    result: dict[str, list] = {}
    verif = 0
    if type(query) != str:
        return {"errors": ["TypeError"]}
    for letter in query.split("&"):
        for el in range(len(letter.split("="))):
            if letter.split("=")[el] != letter.split("=")[-1]:
                result.setdefault(letter.split("=")[el], []).append(
                    letter.split("=")[el + 1]
                )
                verif = 0
            elif letter.split("=")[0] == letter.split("=")[1] and verif == 0:
                result.setdefault(letter.split("=")[el], []).append(
                    letter.split("=")[el]
                )
                verif += 1
    return result


@decor_data
def decodding(code: Any) -> Any:
    if type(code) != str:
        return {"errors": ["TypeError"]}
    if code == "":
        return ""
    if code[-1].isalpha():
        return {"errors": ["NonDigitError"]}
    if code[0].isdigit():
        return {"errors": ["NonLetterError"]}
    list_digit = []
    list_letter = []
    num1 = ""
    for x1 in code:
        if x1.isalpha():
            list_letter.append(x1)
            if num1 != "":
                list_digit.append(num1)
                num1 = ""
        else:
            num1 += x1
    list_digit.append(num1)
    return "".join(x1 * int(z1) for x1, z1 in zip(list_letter, list_digit))


@decor_data
def codding(s1: Any) -> Any:
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
    return result


@decor_data
def rever_dict(d1: Any) -> dict:
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

    return result


@decor_data
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

    return result


@decor_data
def new_set(set1: Any, set2: Any) -> dict:
    if type(set1) != set or type(set2) != set:
        return {"errors": ["TypeError"]}
    return {
        "a&b": set1 & set2,
        "a|b": set1 | set2,
        "a-b": set1 - set2,
        "b-a": set2 - set1,
        "|a-b|": set1 ^ set2,
        "a in b": set1.issubset(set2),
        "b in a": set2.issubset(set1),
    }


@decor_data
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

    return result


if __name__ == "__main__":
    aggression(True)
    aggression(False)
