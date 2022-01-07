from typing import Any
from typing import Dict
from typing import Sequence

Result = Dict[str, Any]


def task_01(arg: str) -> Result:
    if not isinstance(arg, str):
        type_name = type(arg).__name__
        return {"errors": [f"type(arg)={type_name}, MUST be a string"]}

    rev = arg[::-1]
    return {"data": arg == rev}


def task_02(*args: Any) -> Result:
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


def task_03() -> Result:
    return {"data": None}


def task_04() -> Result:
    return {"data": None}


def task_05() -> Result:
    return {"data": None}


def task_06() -> Result:
    return {"data": None}


def task_07() -> Result:
    return {"data": None}


def task_08() -> Result:
    return {"data": None}


def task_09() -> Result:
    return {"data": None}


def task_10() -> Result:
    return {"data": None}


def task_11() -> Result:
    return {"data": None}


def task_12() -> Result:
    return {"data": None}
