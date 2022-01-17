from typing import Any

import pytest

from hw.yaroslav_belaychuk.lesson006HW import zadacha_5

from .common import azaza
from .common import validate_data
from .common import validate_errors

happy_data = [
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "range": (range(10), {}),
        "str-1": ("", {}),
        "str-2": ("a", {}),
        "str-3": ("aaa", {"a": 3}),
        "xdict": (azaza(["aa"], bs=[dict]), {}),
        "xlist": (azaza("aaa", bs=[list]), {"a": 3}),
        "xset": (azaza("aaa", bs=[set]), {}),
        "xtuple": (azaza("aaa", bs=[tuple]), {"a": 3}),
    }.items()
]


@pytest.mark.parametrize("arg,expected", happy_data)
def test_task_05_happy(arg: Any, expected: Any) -> None:
    outcome = zadacha_5(arg)
    validate_data(outcome)

    data = outcome["data"]
    assert data == expected


aza = azaza(bs=[dict])
azz = azaza(bs=[set])

unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "invalid-type": azaza(),
        "unhashable-elms": [aza, aza, azz, azz],
    }.items()
]


@pytest.mark.parametrize("arg", unhappy_data)
def test_task_05_unhappy(arg: Any) -> None:
    outcome = zadacha_5(arg)
    validate_errors(outcome)
