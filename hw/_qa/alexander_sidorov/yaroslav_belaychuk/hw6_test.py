from typing import Any
from typing import Callable

from hw.yaroslav_belaychuk.lesson006HW import zadacha_4
from hw.yaroslav_belaychuk.lesson006HW import zadacha_5
from hw.yaroslav_belaychuk.lesson006HW import zadacha_7


def validate_errors(func: Callable, *args: Any) -> None:
    result = func(*args)

    errors = result.get("errors")
    assert errors
    assert isinstance(errors, list)
    for error in errors:
        assert isinstance(error, str)
    assert errors == sorted(errors)


def test_task_04() -> None:
    validate_errors(zadacha_4, 1)


def test_task_05() -> None:
    assert zadacha_5("") == {"data": {}}
    assert zadacha_5("abc") == {"data": {}}
    assert zadacha_5("aaa") == {"data": {"a": 3}}
    assert zadacha_5({1, 2}) == {"data": {}}
    assert zadacha_5({1: 2}) == {"data": {}}

    validate_errors(zadacha_5, [{}, {}, set()])


def test_task_07() -> None:
    assert zadacha_7("") == {"data": ""}
    assert zadacha_7("a0") == {"data": ""}
    assert zadacha_7("a1") == {"data": "a"}
    assert zadacha_7("a2b2a1") == {"data": "aabba"}

    validate_errors(zadacha_7, "1a1")
    validate_errors(zadacha_7, "a")
