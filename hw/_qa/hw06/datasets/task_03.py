from datetime import date

import pytest

from hw._qa.hw06.common import azaza

today = date.today()
ymd = (today.year - 100, today.month, today.day)

happy_data = [
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "date": [date(*ymd), 100],
        "xdate": [azaza(*ymd, bs=[date]), 100],
    }.items()
]


unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "type-e": ...,
        "type-i": 1,
        "type-n": None,
        "type-x": azaza(),
    }.items()
]
