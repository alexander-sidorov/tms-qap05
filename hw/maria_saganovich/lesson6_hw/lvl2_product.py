import numbers
from typing import Any


def func2_product(*args: Any) -> dict:
    result: dict
    is_error = False
    errors = {"errors": Any}
    product = 1

    for arg in args:
        if isinstance(arg, numbers.Number):
            product *= arg
        else:
            errors["errors"] = ["should be number(s)"]
            is_error = True
            break

    if is_error:
        result = errors
    else:
        result = {"data": product}

    return result
