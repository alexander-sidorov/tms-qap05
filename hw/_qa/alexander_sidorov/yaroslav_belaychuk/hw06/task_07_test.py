from typing import Any

import pytest

from hw.yaroslav_belaychuk.lesson006HW import zadacha_7

from .common import azaza
from .common import validate_data
from .common import validate_errors

happy_data = [
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "empty": ("", ""),
        "str": (azaza("a1", bs=[str]), "a"),
        "v-a1": ("a1", "a"),
        "v-a11": ("a11", "aaaaaaaaaaa"),
        "v-a1b11a1": ("a1b11a1", "abbbbbbbbbbba"),
        "v-a1b2a1": ("a1b2a1", "abba"),
        "v-a3": ("a3", "aaa"),
    }.items()
]


@pytest.mark.parametrize("arg,expected", happy_data)
def test_task_07_happy(arg: Any, expected: Any) -> None:
    outcome = zadacha_7(arg)
    validate_data(outcome)

    data = outcome["data"]
    assert data == expected


unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "invalid-type": azaza(),
        "malformed-1": "1",
        "malformed-1a": "1a",
        "malformed-1a1": "1a1",
        "malformed-a": "a",
        "malformed-aa1": "aa1",
    }.items()
]


@pytest.mark.parametrize("arg", unhappy_data)
def test_task_07_unhappy(arg: Any) -> None:
    outcome = zadacha_7(arg)
    validate_errors(outcome)
