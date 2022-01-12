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


    if args == 0:
        result["errors"] = ["umnojenie na nol"]
    else:
        nakopitel = 1
        for i in args:
            nakopitel *= i

        result["data"] = nakopitel
    return result

