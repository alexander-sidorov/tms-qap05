from typing import Any
from typing import Collection

from .common import Errors
from .common import Result
from .common import Undefined
from .common import build_result
from .common import multiplicative


def task_02(*args: Any) -> Result:
    """
    Multiplies given arguments, from left to right.
    """

    data: Any = Undefined
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
        data = rv

    result = build_result(
        data=data,
        errors=errors,
    )

    return result
