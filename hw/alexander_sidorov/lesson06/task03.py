from datetime import date
from typing import Any
from typing import Literal
from typing import Optional
from typing import Union
from typing import get_args

from .common import Errors
from .common import api

DataKeys = Literal[
    "age",
    "day",
    "month",
    "year",
]

Data = dict[DataKeys, int]


@api
def task_03(arg: date) -> Union[Data, Errors]:
    """
    Composes a birthday info in the specified format.

    Format: {"year": Y, "month": M, "day": D, "age": A},
        where Y, M, D, A are integers.

    Calculates an age, in years.
    """

    errors = validate(arg)
    if errors:
        return errors

    data = {_a: getattr(arg, _a, 0) for _a in get_args(DataKeys)}

    diff = date.today() - arg
    days = diff.days
    years = int(round((days / 365.25)))
    data["age"] = years

    return data


def validate(arg: Any) -> Optional[Errors]:
    if not isinstance(arg, date):
        return {"errors": [f"{type(arg)=}, MUST be a date"]}
    return None
