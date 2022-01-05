from functools import reduce
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


def level_2(*args: Any) -> dict:
    result = {}
    fff = 0
    for i in args:
        if (isinstance(i, int)) is not True:
            fff = 1
    if fff != 0:
        result["errors"] = ["not int"]
    else:
        result["data"] = reduce(lambda x, y: x * y, args)
    return result
