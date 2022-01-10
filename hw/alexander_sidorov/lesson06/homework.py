from typing import Any
from typing import Hashable

from .common import AnySet
from .common import Result
from .common import Undefined
from .common import build_result
from .common import even


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
