from typing import Any

import pytest

from hw.yaroslav_belaychuk.lesson006HW import umnogenie

from .common import azaza
from .common import validate_data
from .common import validate_errors

happy_data = [  # type: ignore  # noqa: ECE001
    pytest.param(args, expected, id=name)  # type: ignore
    for name, (args, expected) in {
        "complex-complex": [(1j, 1j), -1],
        "float-complex": [(2.0, 3j), 6.0j],
        "int-complex": [(2, 3j), 6j],
        "int-float": [(2, 3.0), 6.0],
        "int-int": [(2, 3), 6],
        "int-list-int": [(2, [1], 2), [1, 1, 1, 1]],
        "int-str-int": [(2, "a", 2), "aaaa"],
        "int-str": [(2, "a"), "aa"],
        "int-tuple-int": [(2, (1,), 2), (1, 1, 1, 1)],
        "str-int": [("a", 2), "aa"],
        "str": [("",), ""],
        "xlist-int": [(azaza([1], bs=[list]), 2), [1, 1]],
        "xstr-int": [(azaza("ab", bs=[str]), 2), "abab"],
    }.items()
]


@pytest.mark.parametrize("args,expected", happy_data)
def test_task_02_happy(args: Any, expected: Any) -> None:
    outcome = umnogenie(*args)
    validate_data(outcome)

    data = outcome["data"]
    assert data == expected


unhappy_data = [
    pytest.param(args, id=name)
    for name, args in {
        "invalid-type": [azaza()],
        "not-multiplicative-type": [azaza(), azaza()],
        "not-multiplicative-str-complex": ["a", 2j],
        "not-multiplicative-str-float": ["a", 2.0],
        "not-multiplicative-str-list": ["a", azaza(bs=[list])],
    }.items()
]


@pytest.mark.parametrize("args", unhappy_data)
def test_task_02_unhappy(args: Any) -> None:
    outcome = umnogenie(*args)
    validate_errors(outcome)
