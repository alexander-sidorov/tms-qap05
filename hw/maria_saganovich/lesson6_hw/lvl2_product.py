from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func2_product(*args: Any) -> Any:
    product: Any = 1

    for arg in args:
        if not isinstance(arg, (int, float, complex, str, list, tuple)):
            raise Exception(["Unsupported type"])

        if isinstance(product, (list, str, tuple)) and isinstance(
            arg, (list, tuple, str)
        ):
            raise Exception(["Can't multiply sequence by non-int of types"])

        product *= arg

    return product
