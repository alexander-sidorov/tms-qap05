def strok(abc: str) -> str:
    prabel = abc.find(" ")
    strok1 = abc[:prabel]
    strok2 = abc[prabel + 1 :]  # noqa
    strok3 = strok2 + abc[prabel] + strok1
    return strok3


def lwl1(p1: tuple) -> tuple:
    krt = (p1[0], p1[-1])
    return krt


from typing import Any
from typing import Sequence


def lwl3(
    p1: Sequence,
    p2: Any,
) -> Sequence:
    cpisok = p1[:p2]
    return cpisok


def lwl5(p1: str) -> str:
    otvet = p1.title()
    return otvet
