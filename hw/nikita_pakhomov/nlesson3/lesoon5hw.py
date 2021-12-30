from typing import Any


def strok(abc: str) -> str:
    prabel = abc.find(" ")
    strok1 = abc[:prabel]
    strok2 = abc[prabel + 1 :]  # noqa
    strok3 = strok2 + abc[prabel] + strok1
    return strok3


def lwl1(p1: tuple) -> tuple:
    krt = (p1[0], p1[-1])
    return krt


def lwl3(collection: Any, object_1: Any) -> Any:
    i = collection.index(object_1)
    return collection[: i + 1]


def lwl5(p1: str) -> str:
    otvet = p1.title()
    return otvet
