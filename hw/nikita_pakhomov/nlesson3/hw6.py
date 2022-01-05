from typing import Any


def is_palindrome(text: Any) -> dict:
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
    fff = 0
    for i in args:
        if (isinstance(i, int)) == False: # noqa
            fff = 1
    if fff != 0:
        result["errors"] = ["not int"]
    else:
        result["data"] = sum(args)

    return result
