from functools import reduce
from operator import mul
from typing import Collection
from typing import Optional
from typing import Sequence
from typing import Union
from typing import get_args

from .common import Errors
from .common import ErrorsList
from .common import Multiplicative
from .common import api


@api
def task_02(*args: Multiplicative) -> Union[Multiplicative, Errors]:
    """
    Multiplies given arguments, from left to right.
    """

    if errors := validate(args):
        return errors

    data = reduce(mul, args)

    return data


def validate(args: Collection) -> Optional[Errors]:
    messages: ErrorsList = []

    if not args:
        messages.append("nothing to multiply")

    allowed_types = get_args(Multiplicative)
    nr_cols = 0
    nr_non_ints = 0
    for i, arg in enumerate(args):
        if not isinstance(arg, allowed_types):
            messages.append(f"args[{i}]={arg!r} has unsupported type")

        nr_cols += isinstance(arg, Sequence)
        nr_non_ints += isinstance(arg, (float, complex))

    if nr_cols > 1:
        messages.append(f"cannot multiply {nr_cols} sequences")

    if nr_cols and nr_non_ints:
        messages.append("cannot multiply sequences and non-ints")

    return {"errors": sorted(messages)} if messages else None
