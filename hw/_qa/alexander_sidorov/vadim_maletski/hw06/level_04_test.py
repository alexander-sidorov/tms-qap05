from datetime import date
from typing import Any

import pytest

from hw.vadim_maletski.func6 import level_04

from .common import azaza
from .common import validate_data
from .common import validate_errors

happy_data = [
    pytest.param(*params, id=name)
    for name, params in {
        "date": [{object: date(1900, 1, 1), type: date(1800, 1, 1)}, type],
        "xdate": [
            {
                object: azaza(1900, 1, 1, bs=[date]),
                type: azaza(1800, 1, 1, bs=[date]),
            },
            type,
        ],
    }.items()
]


@pytest.mark.parametrize("arg,expected", happy_data)
def test_task_04_happy(arg: Any, expected: Any) -> None:
    outcome = level_04(arg)
    validate_data(outcome)

    data = outcome["data"]
    assert data == expected


unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "invalid-type": azaza(),
        "empty": {},
    }.items()
]


@pytest.mark.parametrize("arg", unhappy_data)
def test_task_04_unhappy(arg: Any) -> None:
    outcome = level_04(arg)
    validate_errors(outcome)
