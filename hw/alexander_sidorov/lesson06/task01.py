from typing import Any

from .common import Errors
from .common import Result
from .common import Undefined
from .common import build_result


def task_01(arg: str) -> Result:
    """
    Tells if the arg is a palindrome
    """

    data: Any = Undefined
    errors: Errors = []

    if not isinstance(arg, str):
        type_name = type(arg).__name__
        errors.append(f"type(arg)={type_name}, MUST be a string")

    if not errors:
        rev = arg[::-1]
        data = bool(rev == arg)

    result = build_result(
        data=data,
        errors=errors,
    )

    return result
