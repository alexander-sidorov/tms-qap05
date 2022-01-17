from typing import Any
from typing import Optional
from typing import Union

from .common import Errors
from .common import ErrorsList
from .common import api
from .common import even
from .common import hashable


@api
def task_12(*args: Any) -> Union[dict, Errors]:
    """
    Composes a dict from args.
    Even args are treated as keys.
    Odd args are treated as values.
    """

    if errors := validate(args):
        return errors

    data = {}

    for i, elm in enumerate(args):
        if even(i):
            key = elm
            continue

        data[key] = elm

    return data


def validate(args: tuple) -> Optional[Errors]:
    messages: ErrorsList = []

    if (nr_elms := len(args)) % 2 == 1:
        messages.append(f"odd number of elements ({nr_elms})")

    wrong_keys = (
        (i, arg) for i, arg in enumerate(args) if even(i) and not hashable(arg)
    )

    messages.extend(
        f"args[{i}]={key!r} is not hashable" for i, key in wrong_keys
    )

    return {"errors": sorted(messages)} if messages else None
