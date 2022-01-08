from typing import Any


def fun1(collection: Any) -> tuple:
    return collection[0], collection[-1]


def fun2(string: str) -> str:
    string1 = string.rsplit()
    return f"{string1[1]} {string1[0]}"


def fun3(collection1: Any, object3: Any) -> Any:
    collection2 = collection1.index(object3)
    return collection1[: collection2 + 1]


def fun4(string1: str, string_v_1: str) -> str:
    return string_v_1.join(string1)


def fun5(string5: str) -> str:
    return string5.title()
