from typing import Dict
from typing import Hashable
from typing import List
from typing import TypeVar
from typing import Union

from .common import Errors
from .common import Result
from .common import build_result

T1 = TypeVar("T1")
T2 = TypeVar("T2")


def task_09(arg: Dict[T1, T2]) -> Result:
    """
    Reverses the dict.
    Multiple values are composed into a list value.
    """

    if not isinstance(arg, dict):
        return build_result(errors=[f"{type(arg)=!r}, MUST be a dict"])

    data: Dict[T2, Union[T1, List[T1]]] = {}  # noqa: TAE002
    errors: Errors = []

    for key, value in arg.items():
        if not isinstance(value, Hashable):
            _e = f"{value=!r} of {key=!r} cannot be used as a new key"
            errors.append(_e)

        if errors:
            continue

        bucket: List[T1] = data.setdefault(value, [])  # type: ignore
        bucket.append(key)

    if not errors:
        data = {
            value: (bucket if len(bucket) > 1 else bucket[0])  # type: ignore
            for value, bucket in data.items()
        }

    result = build_result(
        data=data,
        errors=errors,
    )

    return result
