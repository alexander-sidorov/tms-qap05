from typing import Any
from typing import Literal
from typing import Optional
from typing import Union

from .common import AnySet
from .common import Errors
from .common import ErrorsList
from .common import api

DataKeys = Literal[
    "|a-b|",
    "a in b",
    "a-b",
    "a&b",
    "a|b",  # type: ignore
    "b in a",
    "b-a",
]

Data = dict[DataKeys, Union[AnySet, bool]]


@api
def task_11(arg1: AnySet, arg2: AnySet) -> Union[Data, Errors]:
    """
    Displays the common set of operations upon two sets.
    """

    if errors := validate(arg1, arg2):
        return errors

    data = {
        "a&b": arg1 & arg2,
        "a|b": arg1 | arg2,
        "a-b": arg1 - arg2,
        "b-a": arg2 - arg1,
        "|a-b|": arg1 ^ arg2,
        "a in b": arg1.issubset(arg2),
        "b in a": arg2.issubset(arg1),
    }

    return data


def validate(arg1: Any, arg2: Any) -> Optional[Errors]:
    messages: ErrorsList = [
        f"arg {i} is {type(arg)}, MUST be a set"
        for i, arg in enumerate((arg1, arg2), start=1)
        if not isinstance(arg, (set, frozenset))
    ]

    return {"errors": sorted(messages)} if messages else None
