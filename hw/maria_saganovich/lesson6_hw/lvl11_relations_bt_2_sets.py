from typing import Any


def func11_relation_bt_2_sets(arg1: Any, arg2: Any) -> dict:
    result = {}
    is_error = False
    result_data = {}
    result_error = []

    if type(arg1) != set:
        result_error.append("arg should be set")
        is_error = True
    elif type(arg2) != set:
        result_error.append("arg should be set")
        is_error = True
    else:
        result_data = {
            "a&b": arg1 & arg2,
            "a|b": arg1 | arg2,
            "a-b": arg1 - arg2,
            "b-a": arg2 - arg1,
            "|a-b|": arg1 ^ arg2,
            "a in b": arg1.issubset(arg2),
            "b in a": arg2.issubset(arg1),
        }

    if is_error:
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
