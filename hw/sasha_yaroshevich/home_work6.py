from typing import Any
from typing import Dict


new_type = Dict[str, Any]
def polindrom_1(stroka: str) -> new_type:
    result = {}

    if type(stroka) != str:
        result["errors"] = ["this is not a string"]
    else:
        if stroka == stroka[::-1]:
            result["data"] = True
        else:
            result["data"] = False
    return result


def proizvedenie_2(*args):
    result = {}


    nakopitel = 1
    for i in args:
        nr = isinstance(nakopitel, (str, list, tuple))
        er = isinstance(i, (str, list, tuple))
        if nr == er:
            result["errors"] = ["stroki, niz9"]
        else:
            nakopitel *= i

        result["data"] = nakopitel
    return result

