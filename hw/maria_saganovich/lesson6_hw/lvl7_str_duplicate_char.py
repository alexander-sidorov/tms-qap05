import re
from typing import Any


def func7_str_duplicate_char(arg: Any) -> dict:
    result: dict[Any, Any] = {}
    is_error = False
    result_data = ""
    result_error = []

    if type(arg) != str:
        result_error.append("arg should be str")
        is_error = True
    else:
        if len(arg) == 0:
            result_error.append("str is empty")
            is_error = True
        else:
            res = re.findall("([a-zA-Z]+\d+)", arg)  # noqa: W605
            for value in res:
                res2 = re.split("(\d+)", value)  # noqa: W605
                result_data += res2[0] * int(res2[1])

    if is_error:
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
