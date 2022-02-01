from typing import Any
from typing import Sequence

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func10_empty_keys_values(arg1: Any, arg2: Any) -> dict:  # noqa: CCR001
    result_data: dict[Any, Any] = {}

    assert isinstance(arg1, Sequence), ["Invalid argument: arg1"]
    assert isinstance(arg2, Sequence), ["Invalid argument: arg2"]

    if len(arg1) > 0 or len(arg2) > 0:
        for index, values in enumerate(list(arg1)):
            result_data[values] = None
            if index < len(arg2):
                result_data[values] = arg2[index]

        if len(arg1) < len(arg2):
            diff = len(arg2) - len(arg1)
            for _key1 in range(len(arg1)):
                result_data[arg1[_key1]] = arg2[_key1]
            for _key2 in range(-diff, 0):
                result_data.setdefault(..., []).append(arg2[_key2])

    return result_data
