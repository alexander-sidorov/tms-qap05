from typing import Any

import pytest

from hw.siarhei_apanel.refakt import decodding

happy_data = [
    pytest.param(*args, id=name)
    for name, args in {
        "1-empty": ("", ""),
        "2-a1": ("a1", "a"),
        "3-a1b2": ("a1b2", "abb"),
        "4-a1b2a1": ("a1b2a1", "abba"),
        "5-a1b11a1": ("a1b11a1", "abbbbbbbbbbba"),
    }.items()
]


@pytest.mark.parametrize("income,expected", happy_data)
def test_task_07_happy_path(income: Any, expected: Any) -> None:
    outcome = decodding(income)
    assert isinstance(outcome, dict)
    assert len(outcome) == 1
    assert "data" in outcome

    data = outcome["data"]
    assert data == expected
