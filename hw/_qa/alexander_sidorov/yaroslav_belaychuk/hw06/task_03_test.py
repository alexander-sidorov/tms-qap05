from datetime import date
from typing import Any

import pytest

from hw.yaroslav_belaychuk.lesson006HW import date_age

from .common import azaza
from .common import validate_data
from .common import validate_errors

today = date.today()
ymd = (today.year - 100, today.month, today.day)

happy_data = [
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "date": [date(*ymd), 100],
        "xdate": [azaza(*ymd, bs=[date]), 100],
    }.items()
]


@pytest.mark.parametrize("arg,expected", happy_data)
def test_task_03_happy(arg: Any, expected: Any) -> None:
    outcome = date_age(arg)
    validate_data(outcome)

    data = outcome["data"]
    assert isinstance(data, dict)
    assert "age" in data

    age = data["age"]
    assert isinstance(age, int)
    assert age == expected


unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "invalid-type": azaza(),
    }.items()
]


@pytest.mark.parametrize("arg", unhappy_data)
def test_task_03_unhappy(arg: Any) -> None:
    outcome = date_age(arg)
    validate_errors(outcome)
