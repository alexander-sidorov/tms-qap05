from functools import wraps
from typing import Any
from typing import Callable


def decor_data(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return {"data": func(*args, **kwargs)}
        except Exception as f:
            return {"errors": [str(f)]}

    return wrapper
