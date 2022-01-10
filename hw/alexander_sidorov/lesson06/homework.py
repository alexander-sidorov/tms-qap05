from itertools import zip_longest
from typing import Any
from typing import Dict
from typing import Hashable
from typing import List
from typing import Optional
from typing import Sequence
from typing import Union

from .common import T1
from .common import T2
from .common import AnySet
from .common import Result
from .common import Undefined
from .common import build_result
from .common import even


def task_09(arg: Dict[T1, T2]) -> Result:
    errors: List[str] = []
    data: Dict[T2, List[T1]] = {}
    result: Result = {}

    for key, value in arg.items():
        if not isinstance(value, Hashable):
            errors.append(
                f"{value=!r} of {key=!r} cannot be used as a new key"
            )

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


def task_10(keys: Sequence[T1], values: Sequence[T2]) -> Result:
    data: Dict[  # noqa: TAE002
        Union[T1, ellipsis],  # noqa: F821
        Union[Optional[T2], List[Optional[T2]]],
    ] = {}
    errors: List[str] = []

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


def task_11(arg1: AnySet, arg2: AnySet) -> Result:
    data = {
        "a&b": arg1 & arg2,
        "a|b": arg1 | arg2,
        "a-b": arg1 - arg2,
        "b-a": arg2 - arg1,
        "|a-b|": arg1 ^ arg2,
        "a in b": arg1.issubset(arg2),
        "b in a": arg2.issubset(arg1),
    }

    return build_result(data=data)


def task_12(*args: Any) -> Result:
    errors = []

    if len(args) % 2 == 1:
        errors.append("odd number of elements")

    data = {}
    key: Any = Undefined

    for i, elem in enumerate(args):
        if even(i):
            if not isinstance(elem, Hashable):
                errors.append(f"args[{i}]={elem!r} is not hashable")
                continue
            key = elem
            continue

        if errors:
            continue

        data[key] = elem

    return build_result(data=data, errors=errors)
