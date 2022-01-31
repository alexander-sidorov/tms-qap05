from typing import Any

import pytest

from hw.vadim_maletski.func6 import level_08

from .common import azaza
from .common import validate_data
from .common import validate_errors

happy_data = [
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "empty": ("", ""),
        "v-a": ("a", "a1"),
        "v-aaa": ("aaa", "a3"),
        "v-aaaaaaaaaaa": ("aaaaaaaaaaa", "a11"),
        "v-abba": ("abba", "a1b2a1"),
        "v-abbbbbbbbbbba": ("abbbbbbbbbbba", "a1b11a1"),
        "xstr": (azaza("a", bs=[str]), "a1"),
    }.items()
]


@pytest.mark.parametrize("arg,expected", happy_data)
def test_task_08_happy(arg: Any, expected: Any) -> None:
    outcome = level_08(arg)
    validate_data(outcome)

    data = outcome["data"]
    assert data == expected


unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "invalid-type": azaza(),
        "malformed-1-x": azaza("1", bs=[str]),
        "malformed-1": "1",
        "malformed-1a": "1a",
        "malformed-1a1": "1a1",
        "malformed-a1": "a1",
        "malformed-aa1": "aa1",
    }.items()
]


@pytest.mark.parametrize("arg", unhappy_data)
def test_task_08_unhappy(arg: Any) -> None:
    outcome = level_08(arg)
    validate_errors(outcome)
