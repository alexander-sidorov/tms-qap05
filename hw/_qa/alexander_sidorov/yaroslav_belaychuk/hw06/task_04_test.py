from typing import Any

import pytest

from hw.yaroslav_belaychuk.lesson006HW import zadacha_4

from .common import azaza
from .common import validate_errors

unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "invalid-type": azaza(),
    }.items()
]


@pytest.mark.parametrize("arg", unhappy_data)
def test_task_04_unhappy(arg: Any) -> None:
    outcome = zadacha_4(arg)
    validate_errors(outcome)
