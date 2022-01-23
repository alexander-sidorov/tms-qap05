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
from .common import Undefined
from .common import api
from .common import validate_args_types

T1 = TypeVar("T1")
T2 = TypeVar("T2")

Data = Dict[
    Union[T1, Literal["..."]],
    Union[Optional[T2], list[Optional[T2]]],
]


@api
@validate_args_types
def task_10(keys: Sequence[T1], values: Sequence[T2]) -> Union[Data, Errors]:
    """
    Composes a dict from the given sequences.
    The first sequence contains keys.
    The second sequence contains values.
    Any extra key is given a None value.
    Any extra value is added to the list of `...` key.
    """

    validate(keys)

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


def validate(keys: Any) -> None:
    for i, key in enumerate(keys):
        assert isinstance(key, Hashable), f"keys[{i}]={key!r} is not hashable"
