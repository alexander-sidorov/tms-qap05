from typing import Any
from typing import Sequence

from hw.alexander_sidorov.lesson06.common import Result


def task_02(*args: Any) -> Result:
    """
    Multiplies given arguments, from left to right.
    """

    if not args:
        return {"errors": ["nothing to multiply"]}

    acc = args[0]

    for arg in args[1:]:
        are_sequences = isinstance(acc, Sequence) and isinstance(arg, Sequence)
        is_acc_ok = isinstance(acc, (Sequence, int, float, complex))
        is_arg_ok = isinstance(arg, (Sequence, int, float, complex))

        if are_sequences or not all((is_acc_ok, is_arg_ok)):
            return {"errors": [f"cannot do: {acc!r} * {arg!r}"]}

        acc = acc * arg

    return {"data": acc}
