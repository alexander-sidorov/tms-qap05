from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func9_swap_keys_values(arg: Any) -> dict:
    result: dict = {}

    if not isinstance(arg, dict):
        raise Exception(["Invalid arg"])

    for _value, key in enumerate(list(arg)):
        if isinstance(arg[key], (list, dict, set, frozenset)):
            raise Exception(["Unhashable arg type"])

        if arg[key] in result:
            result[arg[key]].append(key)
        else:
            result[arg[key]] = [key]

    return result
