from datetime import date
from datetime import datetime
from secrets import choice
from string import ascii_letters
from typing import Any

import pytest
from freezegun import freeze_time

from hw.andrei_bondar.lesson_06hw import datrog


def ololo(*xxx, bs=()) -> Any:
    rs = "".join(choice(ascii_letters) for _ in "_" * 12)
    tyty = type(rs, tuple(bs), {})
    return tyty(*xxx)


happy_data = [
    pytest.param(*args, id=name)
    for name, args in {
        "1-date": (date(1900, 1, 1), 100),
        "2-datetime": (datetime(1900, 1, 1), 100),
        "3-date-sc": (ololo(1900, 1, 1, bs=[date]), 100),
        "4-datetime-sc": (ololo(1900, 1, 1, bs=[datetime]), 100),
    }.items()
]


@freeze_time(date(2000, 1, 1))
@pytest.mark.parametrize("income,expected", happy_data)
def test_task_03_happy_path(income: Any, expected: Any) -> None:
    outcome = datrog(income)
    assert isinstance(outcome, dict)
    assert len(outcome) == 1
    assert "data" in outcome

    data = outcome["data"]
    assert isinstance(data, dict)
    assert "age" in data

    age = data["age"]
    assert age == expected
