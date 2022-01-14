from datetime import date
from typing import Any

from .common import Errors
from .common import Result
from .common import Undefined
from .common import build_result


def task_03(arg: date) -> Result:
    """
    Composes a birthday info in the specified format.

    Format: {"year": Y, "month": M, "day": D, "age": A},
        where Y, M, D, A are integers.

    Calculates an age, in years.
    """

    data: Any = Undefined
    errors: Errors = []

    if not isinstance(arg, date):
        errors.append(f"{type(arg)=}, MUST be a date")

    if not errors:
        diff = date.today() - arg
        days = diff.days
        years = int(round((days / 365.25)))
        data = {_a: getattr(arg, _a) for _a in {"year", "month", "day"}}
        data["age"] = years

    result = build_result(
        data=data,
        errors=errors,
    )

    return result
