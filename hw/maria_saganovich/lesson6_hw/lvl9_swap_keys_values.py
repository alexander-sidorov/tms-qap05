from typing import Any


def func9_swap_keys_values(arg: Any) -> dict:
    result: dict = {}

    if type(arg) != dict:
        return {"errors": ["Unsupported type"]}

    for _value, key in enumerate(list(arg)):
        if type(arg[key]) == list and len(arg[key]) == 0:
            return {"errors": ["List is empty"]}
        if arg[key] in result:
            result[arg[key]].append(key)
        else:
            result[arg[key]] = [key]

    return {"data": result}
