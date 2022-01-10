from itertools import zip_longest
from typing import Any
from typing import Dict
from typing import Hashable
from typing import List
from typing import Optional
from typing import Sequence
from typing import TypeVar
from typing import Union

from .common import Errors
from .common import Result
from .common import Undefined
from .common import build_result

T1 = TypeVar("T1")
T2 = TypeVar("T2")


def task_10(keys: Sequence[T1], values: Sequence[T2]) -> Result:
    """
    Composes a dict from the given sequences.
    The first sequence contains keys.
    The second sequence contains values.
    Any extra key is given a None value.
    Any extra value is added to the list of `...` key.
    """

    data: Dict[  # noqa: TAE002
        Union[T1, ellipsis],  # noqa: F821
        Union[Optional[T2], List[Optional[T2]]],
    ] = {}
    errors: List[str] = []

    validate_args(keys, values, errors)
    if errors:
        return build_result(errors=errors)

    pairs = zip_longest(keys, values, fillvalue=Undefined)
    anon_values: List[Optional[T2]] = []

    for i, (key, value) in enumerate(pairs):
        if not isinstance(key, Hashable):
            errors.append(f"keys[{i}]={key!r} is not hashable")

        if errors:
            continue

        if key is Undefined:
            anon_values.append(value)
            continue

        if value is Undefined:
            value = None

        data[key] = value

    if not errors and anon_values:
        data[...] = anon_values

    return build_result(data=data, errors=errors)


def validate_args(keys: Any, values: Any, errors: Errors) -> None:
    if not isinstance(keys, Sequence):
        errors.append(f"{type(keys)=!r}, MUST be a sequence")

    if not isinstance(values, Sequence):
        errors.append(f"{type(values)=!r}, MUST be a sequence")
