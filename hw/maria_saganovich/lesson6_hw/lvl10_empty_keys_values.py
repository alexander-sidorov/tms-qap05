from typing import Any


def func10_empty_keys_values(arg1: Any, arg2: Any) -> dict:
    result_data: dict[Any, Any] = {}

    if type(arg1) == str or type(arg2) == list:
        for index, values in enumerate(list(arg1)):
            if index < len(arg2):
                result_data[values] = arg2[index]
            else:
                result_data[values] = None
        if len(arg1) < len(arg2):
            result_data[...] = arg2[len(arg1) : len(arg2) + 1]  # noqa: E203

    return {"data": result_data}
