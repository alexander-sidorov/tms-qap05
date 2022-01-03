from typing import Any


def polindrom(stroka: str) -> Any:
    result = {}

    if type(stroka) != str:
        result["errors"] = ["this is not a string"]
    else:
        if stroka == stroka[::-1]:
            result["data"] = True
        else:
            result["data"] = False
    return result
