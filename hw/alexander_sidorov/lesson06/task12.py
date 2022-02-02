from typing import Any
from typing import Union

from hw.alexander_sidorov.common import Errors
from hw.alexander_sidorov.common import api
from hw.alexander_sidorov.common import even
from hw.alexander_sidorov.common import hashable
from hw.alexander_sidorov.common import typecheck


@api
@typecheck
def task_12(*args: Any) -> Union[dict, Errors]:
    """
    Composes a dict from args.
    Even args are treated as keys.
    Odd args are treated as values.
    """

    validate(args)

    data = {}

    for i, elm in enumerate(args):
        if even(i):
            key = elm
            continue

        data[key] = elm

    return data


def validate(args: tuple) -> None:
    nr_elms = len(args)

    assert nr_elms % 2 != 1, f"odd number of elements ({nr_elms})"

    for i, arg in enumerate(args):
        if even(i):
            assert hashable(arg), f"args[{i}]={arg!r} is not hashable"
