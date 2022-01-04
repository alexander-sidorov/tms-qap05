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
