from typing import Any


def lvl_1(collection: Any) -> tuple:
    return collection[0], collection[-1]


def lvl_2(phrase: str) -> str:
    exchange = phrase.rsplit()
    return f"{exchange[1]} {exchange[0]}"


def lvl_3(collection3: Any, object3: Any) -> Any:
    new_collection = collection3.index(object3)
    return collection3[: new_collection + 1]


def lvl_4(some_string: str, symbol: str) -> str:
    new_string = "".join(x + symbol for x in some_string)
    return new_string[0:-1]


def lvl_5(string_to_be_capitalized: str) -> str:
    return string_to_be_capitalized.title()
