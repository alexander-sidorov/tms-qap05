from collections.abc import Iterable
from collections.abc import Sequence
from datetime import date
from functools import reduce
from functools import wraps
from typing import Any
from typing import Callable
from typing import Collection


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


def decor_data(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return {"data": func(*args, **kwargs)}
        except Exception as f:
            return {"errors": [str(f)]}

    return wrapper


@decor_data
def palindrom(di1: Any) -> Any:
    assert isinstance(di1, str), "No String"
    return di1[:] == di1[::-1]


@decor_data
def proizvedenie(*args: Any) -> Any:
    if len(args) == 1:
        assert not isinstance(args[0], type), "No Class"
        assert args[0] not in [[], (), {}, set(), frozenset()], "No Arguments"
        if not isinstance(args[0], Iterable):
            return args[0]
        for _i in args[0]:
            return args[0]
    return reduce(lambda x, y: x * y, args)


@decor_data
def dateday(yer: Any) -> Any:
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
    assert isinstance(yer, dict), "No Match Type"
    return min(yer, key=lambda t: yer[t])


@decor_data
def repeat(collect: Any) -> dict:
    assert isinstance(collect, Collection), "No Collections"
    if isinstance(collect, (set, dict)) or len(collect) < 2:
        return {}
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
    assert isinstance(query, str), "No String"
    if len(query) < 2:
        return {}
    if "=" not in query:
        return {query: [""]}
    result: dict[str, list] = {}
    for letter in query.split("&"):
        verif = letter.index("=")
        new_letter = letter[:verif]
        if new_letter not in result:
            result[new_letter] = [letter[verif + 1 :]]  # noqa: E203
        else:
            result[new_letter].append(letter[verif + 1 :])  # noqa: E203
    return result


@decor_data
def decodding(code: Any) -> Any:
    assert isinstance(code, str), "No String"
    if code == "":
        return ""
    assert code[-1].isdigit(), "None Digital"
    assert code[0].isalpha(), "None Letter"
    list_digit = []
    list_letter = []
    num1 = ""
    for x1 in range(len(code)):
        if (
            code[x1].isalpha()
            and code[x1] != code[-1]  # noqa: W503
            and code[x1 + 1].isalpha()  # noqa: W503
        ):
            raise Exception("None Next Digital")
        if code[x1].isalpha():
            list_letter.append(code[x1])
            if num1 != "":
                list_digit.append(num1)
                num1 = ""
        else:
            num1 += code[x1]
    list_digit.append(num1)
    return "".join(x2 * int(z1) for x2, z1 in zip(list_letter, list_digit))


@decor_data
def codding(s1: Any) -> Any:
    assert isinstance(s1, str), "No String"
    i1 = 0
    num = 0
    result = ""
    for i1 in range(len(s1)):
        assert s1[i1].isalpha(), "None Letter"
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
    assert isinstance(d1, dict), "No DictionType"
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
def new_dict(key: Any, value: Any) -> dict:  # noqa: CCR001
    assert isinstance(key, Sequence), "Key No Sequence"
    assert isinstance(value, Sequence), "Value No Sequence"
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
    assert isinstance(set1, (frozenset, set)), "No Set"
    assert isinstance(set2, (frozenset, set)), "No Set"
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
    if len(digit) < 2 and not bool(digit[0]):
        return {}
    assert len(digit) % 2 == 0, "No Pair"
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
