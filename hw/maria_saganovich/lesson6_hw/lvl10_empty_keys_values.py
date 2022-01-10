from typing import Any


def func10_empty_keys_values(arg1: Any, arg2: Any) -> dict:  # noqa: CCR001
    result: dict[str, Any] = {}
    is_error = False
    result_data: dict[Any, Any] = {}
    result_error = []

    if type(arg1) != str or type(arg2) != list:
        result_error.append("incorrect arg")
        is_error = True
    else:
        if len(arg1) == 0 and len(arg2) == 0:
            result_error.append("is undefined")
            is_error = True
        else:
            for index, values in enumerate(list(arg1)):
                if index < len(arg2):
                    result_data[values] = arg2[index]
                else:
                    result_data[values] = None

            if len(arg1) < len(arg2):
                result_data[...] = arg2[
                    len(arg1) : len(arg2) + 1  # noqa: E203
                ]

    if is_error:
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
