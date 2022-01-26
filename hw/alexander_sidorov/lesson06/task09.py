from typing import Any
from typing import List
from typing import TypeVar
from typing import Union

from .common import Errors
from .common import api
from .common import hashable
from .common import typecheck

T1 = TypeVar("T1")
T2 = TypeVar("T2")

ForwardDict = dict[T1, T2]
ReversedDict = dict[T2, Union[T1, List[T1]]]


@api
@typecheck
def task_09(arg: ForwardDict) -> Union[ReversedDict, Errors]:
    """
    Reverses the dict.
    Multiple values are composed into a list value.
    """

    validate(arg)

    data: ForwardDict = {}

    for key, value in arg.items():
        bucket = data.setdefault(value, [])
        bucket.append(key)

    data = {
        value: (bucket if len(bucket) > 1 else bucket[0])
        for value, bucket in data.items()
    }

    return data


def validate(arg: Any) -> None:
    for key, value in arg.items():
        assert hashable(
            value
        ), f"{value=!r} of {key=!r} cannot be used as a new key"
