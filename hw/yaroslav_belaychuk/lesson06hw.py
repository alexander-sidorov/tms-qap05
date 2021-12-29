from typing import Any


def cortage(a1: list) -> tuple:
    return a1[0], a1[-1]


def string(b1: str) -> str:
    b2 = b1.split()
    new_word = b2[1] + " " + b2[0]
    return new_word


def collection(c1: list, c2: Any) -> list:  # type:  ignore
    c1.append(c2)
    return c1


def str_in_str(d1: str, d2: str) -> str:
    string = d2.join(d1)
    return string


def string_zaglavie(q1: str) -> str:
    return q1.title()
