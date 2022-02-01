from typing import Any


def my_func_decorator(some_func: Any) -> Any:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return {"data": some_func(*args, **kwargs)}
        except Exception as e:
            return {"errors": e.args[0]}

    return wrapper
