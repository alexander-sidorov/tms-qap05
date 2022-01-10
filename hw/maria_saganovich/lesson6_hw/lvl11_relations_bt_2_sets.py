from typing import Any


def func11_relation_bt_2_sets(arg1: Any, arg2: Any) -> dict:
    result: dict[Any, Any] = {}
    result_data = {}
    result_error = []

    if type(arg1) != set or type(arg2) != set:
        result_error.append("arg should be set")
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

    if bool(result_error):
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
