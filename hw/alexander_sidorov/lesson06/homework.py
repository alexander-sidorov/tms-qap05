import re
from itertools import groupby
from itertools import zip_longest
from typing import Any
from typing import Dict
from typing import Hashable
from typing import List
from typing import Optional
from typing import Sequence
from typing import Union
from urllib.parse import parse_qs

from .common import T1
from .common import T2
from .common import AnySet
from .common import Result
from .common import Undefined
from .common import build_result
from .common import even


def task_06(query: str) -> Result:
    parsed = parse_qs(
        query,
        keep_blank_values=True,
    )
    return {"data": parsed}


def task_07(folded_text: str) -> Result:
    folds = re.findall(r"(\D\d+)", folded_text)
    if "".join(folds) != folded_text:
        return {"errors": [f"{folded_text=!r} is malformed"]}

    chars_counts = ((fold[0], int(fold[1:])) for fold in folds)

    flatten_text = "".join(char * count for char, count in chars_counts)

    return {"data": flatten_text}


def task_08(flatten_text: str) -> Result:
    if re.match(r".*\d", flatten_text):
        return {"errors": ["integers MUST not be present in flatten text"]}

    folded_text = "".join(
        f"{char}{len(list(group))}" for char, group in groupby(flatten_text)
    )

    return {"data": folded_text}


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
