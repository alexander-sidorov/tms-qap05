from typing import Any

import pytest

from hw.vadim_maletski.func6 import level_01

from .common import azaza
from .common import validate_data
from .common import validate_errors

happy_data = [
    pytest.param(*params, id=name)
    for name, params in {
        "empty": ["", True],
        "str-0": [azaza("ab", bs=[str]), False],
        "str-1": [azaza("aa", bs=[str]), True],
        "v-Aa_a": ["Aa a", False],
        "v-Aa": ["Aa", False],
        "v-aa": ["aa", True],
        "v-aaa": ["aaa", True],
        "v-ab": ["ab", False],
        "v-aba": ["aba", True],
    }.items()
]


@pytest.mark.parametrize("arg,expected", happy_data)
def test_task_01_happy(arg: Any, expected: Any) -> None:
    outcome = level_01(arg)
    validate_data(outcome)

    data = outcome["data"]  # pylint: disable=unsubscriptable-object
    assert data == expected


unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "invalid-type": azaza(),
    }.items()
]


@pytest.mark.parametrize("arg", unhappy_data)
def test_task_01_unhappy(arg: Any) -> None:
    outcome = level_01(arg)
    validate_errors(outcome)
