from typing import Any


def func2_product(*args: Any) -> dict:
    product: Any = 1

    for arg in args:
        if not isinstance(arg, (int, float, complex, str, list)):
            return {"errors": "Unsupported type"}

        if isinstance(product, (list, str)) and isinstance(arg, (list, str)):
            return {"errors": "Can't multiply sequence by non-int of types"}

        product *= arg

    return {"data": product}
