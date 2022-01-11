from typing import Any
from typing import Dict

type_1 = Dict[str, Any]


def is_palindrome(text: str) -> type_1:
    result = {}
    if type(text) == str:
        if text[::-1] == text:
            result["data"] = True
        else:
            result["data"] = False
    else:
        result["errors"] = ["not string"]
    return result


def level_2(*args):
    result = {}

    if args == 0:
        result["errors"] = ["delenie na nol"]
    else:
        nakopitel = 1
        for i in args:
            nakopitel *= i

        result["data"] = nakopitel
    return result
