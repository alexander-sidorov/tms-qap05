from typing import Any
from typing import Hashable

from .common import Result
from .common import Undefined
from .common import build_result
from .common import even


def task_12(*args: Any) -> Result:
    """
    Composes a dict from args
    Even args are treated as keys
    Odd args are treated as values
    """

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
