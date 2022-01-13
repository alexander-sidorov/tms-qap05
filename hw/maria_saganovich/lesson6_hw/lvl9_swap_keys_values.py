from typing import Any


def func9_swap_keys_values(arg: Any) -> dict:
    result: dict = {}

    if not isinstance(arg, dict):
        return {"errors": ["Invalid arg"]}

    for _value, key in enumerate(list(arg)):
        if isinstance(arg[key], (list, dict, set, frozenset)):
            return {"errors": ["Unhashable arg type"]}

        if arg[key] in result:
            result[arg[key]].append(key)
        else:
            result[arg[key]] = [key]

    return {"data": result}
