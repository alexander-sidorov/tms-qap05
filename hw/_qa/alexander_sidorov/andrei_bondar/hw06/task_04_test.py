from datetime import date
from typing import Any

import pytest

from hw.andrei_bondar.lesson_06hw import ber4

from .task_03_test import ololo

unhappy_data = [
    pytest.param(*args, id=name)
    for name, args in {
        "1-not-comparable": [{2: ololo(), 1: ololo()}],
        "2-invalid-type": [ololo()],
    }.items()
]


@pytest.mark.parametrize("income", unhappy_data)
def test_task_04_unhappy(income: Any) -> None:
    outcome = ber4(income)
    assert isinstance(outcome, dict)
    assert len(outcome) == 1
    assert "errors" in outcome

    errors = outcome["errors"]
    assert errors
    assert isinstance(errors, list)
    for error in errors:
        assert isinstance(error, str)
    assert errors == sorted(errors)
