from datetime import date

from .common import Result


def task_03(arg: date) -> Result:
    """
    Composes a birthday info in the specified format.

    Format: {"year": Y, "month": M, "day": D, "age": A},
        where Y, M, D, A are integers.

    Calculates an age, in years.
    """

    diff = date.today() - arg
    days = diff.days
    years = int(round((days / 365.25)))
    data = {_a: getattr(arg, _a) for _a in {"year", "month", "day"}}

    return {"data": data | {"age": years}}
