from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func12_even_keys_odd_values(*args: Any) -> dict:
    result_data: dict[Any, Any] = {}
    odd_args = []
    even_args = []

    if len(args) % 2 == 1:
        raise Exception(["should be even count"])
    for key, arg in enumerate(args, start=1):
        if key % 2 == 1:
            odd_args.append(arg)
        else:
            even_args.append(arg)

    for index, value in enumerate(odd_args):
        if isinstance(value, (list, dict, set, frozenset)):
            raise Exception(["Unhashable type: 'list'"])

        result_data[value] = even_args[index]

    return result_data
