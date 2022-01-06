from typing import Any
from datetime import date


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


if __name__ == "__main__":
    aggression(True)
    aggression(False)
