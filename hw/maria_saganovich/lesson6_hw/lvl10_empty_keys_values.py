from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func10_empty_keys_values(arg1: Any, arg2: Any) -> dict:
    result_data: dict[Any, Any] = {}

    if isinstance(arg1, (dict, set, frozenset)) or isinstance(
        arg2, (dict, set, frozenset)
    ):
        raise Exception(["Invalid arguments"])

    if len(arg1) > 0 or len(arg2) > 0:
        for index, values in enumerate(list(arg1)):
            if index < len(arg2):
                result_data[values] = arg2[index]
            else:
                result_data[values] = None
        if len(arg1) < len(arg2):
            result_data[...] = arg2[len(arg1) : len(arg2) + 1]  # noqa: E203

    return result_data
