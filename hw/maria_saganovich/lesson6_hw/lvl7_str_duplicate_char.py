import re
from typing import Any


def func7_str_duplicate_char(arg: Any) -> dict:
    result: dict[Any, Any] = {}
    result_data = ""
    result_error = []

    if type(arg) != str or len(arg) == 0:
        result_error.append("Invalid argument")
    else:
        res = re.findall("([a-zA-Z]+\\d+)", arg)
        for value in res:
            res2 = re.split("(\\d+)", value)
            result_data += res2[0] * int(res2[1])

    if bool(result_error):
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
