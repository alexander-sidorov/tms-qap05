from typing import Any
from typing import List
from typing import Optional
from typing import TypeVar
from typing import Union

from .common import Errors
from .common import ErrorsList
from .common import api
from .common import hashable

T1 = TypeVar("T1")
T2 = TypeVar("T2")

ForwardDict = dict[T1, T2]
ReversedDict = dict[T2, Union[T1, List[T1]]]


@api
def task_09(arg: ForwardDict) -> Union[ReversedDict, Errors]:
    """
    Reverses the dict.
    Multiple values are composed into a list value.
    """

    if errors := validate(arg):
        return errors

    data: ForwardDict = {}

    for key, value in arg.items():
        bucket = data.setdefault(value, [])
        bucket.append(key)

    data = {
        value: (bucket if len(bucket) > 1 else bucket[0])
        for value, bucket in data.items()
    }

    return data


def validate(arg: Any) -> Optional[Errors]:
    messages: ErrorsList = []

    if not isinstance(arg, dict):
        messages.append(f"{type(arg)=!r}, MUST be a dict")
    else:
        for key, value in arg.items():
            if not hashable(value):
                _e = f"{value=!r} of {key=!r} cannot be used as a new key"
                messages.append(_e)

    return {"errors": sorted(messages)} if messages else None
