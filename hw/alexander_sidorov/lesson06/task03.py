from datetime import date
from typing import Literal
from typing import Union
from typing import get_args

from .common import Errors
from .common import api
from .common import validate_args_types

DataKeys = Literal[
    "age",
    "day",
    "month",
    "year",
]

Data = dict[DataKeys, int]


@api
@validate_args_types
def task_03(arg: date) -> Union[Data, Errors]:
    """
    Composes a birthday info in the specified format.

    Format: {"year": Y, "month": M, "day": D, "age": A},
        where Y, M, D, A are integers.

    Calculates an age, in years.
    """

    data = {_a: getattr(arg, _a, 0) for _a in get_args(DataKeys)}

    diff = date.today() - arg
    days = diff.days
    years = int(round((days / 365.25)))
    data["age"] = years

    return data
