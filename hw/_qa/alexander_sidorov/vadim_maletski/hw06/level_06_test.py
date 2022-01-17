from typing import Any

import pytest

from hw.vadim_maletski.func6 import level_06

from .common import azaza
from .common import validate_data
from .common import validate_errors

happy_data = [  # noqa: ECE001
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "empty-1": ("", {}),
        "empty-2": (azaza("", bs=[str]), {}),
        "v-0": ("xx", {"xx": [""]}),
        "v-1": ("xx=", {"xx": [""]}),
        "v-2": ("xx=&yy=", {"xx": [""], "yy": [""]}),
        "v-3": ("xx=1&yy=2&yy=3", {"xx": ["1"], "yy": ["2", "3"]}),
        "v-4": ("xx=xx&yy=yy&yy=yy", {"xx": ["xx"], "yy": ["yy", "yy"]}),
        "v-5": ("xx=xx&yy=yy&yy=", {"xx": ["xx"], "yy": ["yy", ""]}),
    }.items()
]


@pytest.mark.parametrize("arg,expected", happy_data)
def test_task_06_happy(arg: Any, expected: Any) -> None:
    outcome = level_06(arg)
    validate_data(outcome)

    data = outcome["data"]
    assert data == expected


unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "invalid-type": azaza(),
    }.items()
]


@pytest.mark.parametrize("arg", unhappy_data)
def test_task_06_unhappy(arg: Any) -> None:
    outcome = level_06(arg)
    validate_errors(outcome)
