from typing import Any
from typing import Collection

from .common import Errors
from .common import api
from .common import build_result
from .common import multiplicative


@api
def task_02(*args: Any) -> Any:
    """
    Multiplies given arguments, from left to right.
    """

    errors: Errors = []

    if not args:
        errors.append("nothing to multiply")
        return build_result(errors=errors)

    rv = args[0]

    for lv in args[1:]:
        both_colls = isinstance(rv, Collection) and isinstance(lv, Collection)
        rvalue_mul = multiplicative(rv)
        lvalue_mul = multiplicative(lv)

        if both_colls or not all((rvalue_mul, lvalue_mul)):
            errors.append(f"cannot do: {rv!r} * {lv!r}")
            continue

        rv *= lv

    if not errors:
        return rv

    return build_result(errors=errors)
