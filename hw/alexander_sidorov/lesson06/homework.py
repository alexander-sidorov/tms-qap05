import re
from collections import Counter
from datetime import date
from itertools import groupby
from itertools import zip_longest
from typing import Any
from typing import Collection
from typing import Dict
from typing import Hashable
from typing import List
from typing import Optional
from typing import Sequence
from typing import TypeVar
from typing import Union
from urllib.parse import parse_qs

Result = Dict[str, Any]

T1 = TypeVar("T1")
T2 = TypeVar("T2")


class UndefinedType:
    pass


Undefined = UndefinedType()


def build_result(
    *,
    data: Any = Undefined,
    errors: Union[List[str], UndefinedType] = Undefined,
) -> Result:
    result: Result = {}

    if errors and errors is not Undefined:
        assert isinstance(errors, list)
        result["errors"] = sorted(errors)

    if not result and data is not Undefined:
        result["data"] = data

    return result


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


def task_11() -> Result:
    return {"data": None}


def task_12() -> Result:
    return {"data": None}
