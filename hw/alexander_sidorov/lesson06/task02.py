from functools import reduce
from operator import mul
from typing import Collection
from typing import Sequence
from typing import Union

from .common import Errors
from .common import Multiplicative
from .common import api
from .common import validate_args_types


@api
@validate_args_types
def task_02(*args: Multiplicative) -> Union[Multiplicative, Errors]:
    """
    Multiplies given arguments, from left to right.
    """

    validate(args)

    data = reduce(mul, args)

    return data


def validate(args: Collection) -> None:
    assert args, "nothing to multiply"

    nr_cols = 0
    nr_non_ints = 0
    for arg in args:
        nr_cols += isinstance(arg, Sequence)
        nr_non_ints += isinstance(arg, (float, complex))

    assert nr_cols <= 1, f"cannot multiply {nr_cols} sequences"

    assert (
        not nr_cols or not nr_non_ints
    ), "cannot multiply sequences and non-ints"
