from typing import Any

from .common import AnySet
from .common import Errors
from .common import Result
from .common import build_result


def task_11(arg1: AnySet, arg2: AnySet) -> Result:
    """
    Displays the common set of operations on two sets.
    """

    errors: Errors = []
    validate_args(arg1, arg2, errors)
    if errors:
        return build_result(errors=errors)

    data = {
        "a&b": arg1 & arg2,
        "a|b": arg1 | arg2,
        "a-b": arg1 - arg2,
        "b-a": arg2 - arg1,
        "|a-b|": arg1 ^ arg2,
        "a in b": arg1.issubset(arg2),
        "b in a": arg2.issubset(arg1),
    }

    return build_result(data=data)


def validate_args(arg1: Any, arg2: Any, errors: Errors) -> None:
    if not isinstance(arg1, (set, frozenset)):
        errors.append(f"{type(arg1)=!r}, MUST be a set")

    if not isinstance(arg2, (set, frozenset)):
        errors.append(f"{type(arg2)=!r}, MUST be a set")
