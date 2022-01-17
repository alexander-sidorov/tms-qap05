from itertools import zip_longest
from typing import Any
from typing import Dict
from typing import Hashable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import TypeVar
from typing import Union

from .common import Errors
from .common import ErrorsList
from .common import Undefined
from .common import api

T1 = TypeVar("T1")
T2 = TypeVar("T2")

Data = Dict[
    Union[T1, Literal["..."]],
    Union[Optional[T2], list[Optional[T2]]],
]


@api
def task_10(keys: Sequence[T1], values: Sequence[T2]) -> Union[Data, Errors]:
    """
    Composes a dict from the given sequences.
    The first sequence contains keys.
    The second sequence contains values.
    Any extra key is given a None value.
    Any extra value is added to the list of `...` key.
    """

    if errors := validate(keys, values):
        return errors

    pairs = zip_longest(keys, values, fillvalue=Undefined)

    data: Data = {}
    for key, value in pairs:
        if key is Undefined:
            data.setdefault(..., []).append(value)  # type: ignore
            continue

        if value is Undefined:
            value = None

        data[key] = value

    return data


def validate(keys: Any, values: Any) -> Optional[Errors]:
    errors: ErrorsList = []

    if not isinstance(keys, Sequence):
        errors.append(f"{type(keys)=!r}, MUST be a sequence")
    else:
        for i, key in enumerate(keys):
            if not isinstance(key, Hashable):
                errors.append(f"keys[{i}]={key!r} is not hashable")

    if not isinstance(values, Sequence):
        errors.append(f"{type(values)=!r}, MUST be a sequence")

    return {"errors": sorted(errors)} if errors else None
