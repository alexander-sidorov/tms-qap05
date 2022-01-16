from datetime import date
from typing import Any

from .common import Errors
from .common import api
from .common import build_result


@api
def task_03(arg: date) -> Any:
    """
    Composes a birthday info in the specified format.

    Format: {"year": Y, "month": M, "day": D, "age": A},
        where Y, M, D, A are integers.

    Calculates an age, in years.
    """

    errors: Errors = []

    if not isinstance(arg, date):
        errors.append(f"{type(arg)=}, MUST be a date")

    if not errors:
        diff = date.today() - arg
        days = diff.days
        years = int(round((days / 365.25)))
        data = {_a: getattr(arg, _a) for _a in {"year", "month", "day"}}
        data["age"] = years

        return data

    return build_result(errors=errors)
