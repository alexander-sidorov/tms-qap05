from typing import Dict
from typing import Hashable
from typing import List
from typing import TypeVar

from .common import Result

T1 = TypeVar("T1")
T2 = TypeVar("T2")


def task_09(arg: Dict[T1, T2]) -> Result:
    """
    Reverses the dict.
    Multiple values are composed into a list value.
    """

    errors: List[str] = []
    data: Dict[T2, List[T1]] = {}
    result: Result = {}

    for key, value in arg.items():
        if not isinstance(value, Hashable):
            _e = f"{value=!r} of {key=!r} cannot be used as a new key"
            errors.append(_e)

        if errors:
            continue

        bucket: List[T1] = data.setdefault(value, [])
        bucket.append(key)

    if errors:
        result["errors"] = sorted(errors)
    else:
        data_ = {
            value: (bucket if len(bucket) > 1 else bucket[0])
            for value, bucket in data.items()
        }
        result["data"] = data_

    return result
