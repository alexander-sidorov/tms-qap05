from typing import Any

from .common import Errors
from .common import api


@api
def task_01(arg: str) -> Any:
    """
    Tells if the arg is a palindrome
    """

    errors: Errors = []

    if not isinstance(arg, str):
        type_name = type(arg).__name__
        errors.append(f"type(arg)={type_name}, MUST be a string")

    if not errors:
        rev = arg[::-1]
        data = bool(rev == arg)
        return data

    return {"errors": errors}
