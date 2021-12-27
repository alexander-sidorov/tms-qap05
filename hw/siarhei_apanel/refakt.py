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


<<<<<<< HEAD
def korteg(spisok: list) -> tuple:
    return (spisok[0], spisok[-1])


def newwords(words: str) -> str:
    words1 = words.split()
    return words1[1] + " " + words1[0]


def srez(spisk: list, another: Any) -> list:
    spisk.append(another)
    return spisk


def stroki(stroka: str, stroka2: str) -> str:
    return "".join(lit + stroka2 for lit in stroka)


def zaglav(stroka: str) -> str:
    return stroka.title()


def krypto(cod: str, key: str) -> str:
    alphavit = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ind = []
    for i1 in cod:
        if i1 == " ":
            ind.append(i1)
        else:
            ind.append(alphavit[key.find(i1)])

    return " ".join(ind)


=======
>>>>>>> main
if __name__ == "__main__":
    aggression(True)
