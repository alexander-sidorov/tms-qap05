from collections import Counter
from datetime import date
from typing import Any
from typing import Collection
from typing import Dict
from typing import Hashable
from typing import List
from typing import Sequence
from typing import TypeVar
from urllib.parse import parse_qs

Result = Dict[str, Any]

T1 = TypeVar("T1")


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


def task_03(arg: date) -> Result:
    diff = date.today() - arg
    days = diff.days
    years = int(round((days / 365.25)))
    data = {_a: getattr(arg, _a) for _a in {"year", "month", "day"}}
    return {"data": data | {"age": years}}


def task_04(birthdays: Dict[T1, date]) -> Result:
    name: T1
    _birthday: date
    name, _birthday = min(
        birthdays.items(),
        key=lambda _pair: _pair[1],
    )

    return {"data": name}


def task_05(collection: Collection[T1]) -> Result:
    elem: T1

    errors: List[str] = []

    for i, elem in enumerate(collection):
        if not isinstance(elem, Hashable):
            errors.append(f"collection[{i}]={elem!r} is not hashable")

    if errors:
        return {"errors": errors}

    ctr = Counter(collection)
    data = {elem: count for elem, count in ctr.items() if count > 1}
    return {"data": data}


def task_06(query: str) -> Result:
    parsed = parse_qs(
        query,
        keep_blank_values=True,
    )
    return {"data": parsed}


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
