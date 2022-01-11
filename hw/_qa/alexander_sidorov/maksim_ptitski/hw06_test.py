from secrets import choice
from string import ascii_letters
from typing import Any
from typing import Callable

from hw.maksim_ptitski.lesson6_hw import data_multiplication
from hw.maksim_ptitski.lesson6_hw import how_old_are_you
from hw.maksim_ptitski.lesson6_hw import is_the_string_is_the_palindrome
from hw.maksim_ptitski.lesson6_hw import repeated_symbols
from hw.maksim_ptitski.lesson6_hw import the_oldest_one


def kek() -> Any:
    return type("".join(choice(ascii_letters) for _ in "_" * 24), (), {})()


def validate_errors(func: Callable, *args: Any) -> None:
    result = func(*args)
    errors = result.get("errors")
    assert errors
    assert isinstance(errors, list)
    for error in errors:
        assert isinstance(error, str)
    assert errors == sorted(errors)


def test_task_01() -> None:
    validate_errors(
        is_the_string_is_the_palindrome,
        kek(),
    )


def test_task_02() -> None:
    validate_errors(
        data_multiplication,
    )

    validate_errors(
        data_multiplication,
        "a",
        2,
        "a",
    )


def test_task_03() -> None:
    validate_errors(
        how_old_are_you,
        kek(),
    )

    validate_errors(
        how_old_are_you,
        {1: kek()},
    )


def test_task_04() -> None:
    validate_errors(
        the_oldest_one,
        kek(),
    )


def test_task_05() -> None:
    assert repeated_symbols("") == {"data": {}}
    assert repeated_symbols("a") == {"data": {}}
    assert repeated_symbols("ab") == {"data": {}}
    assert repeated_symbols("aa") == {"data": {"a": 2}}

    validate_errors(
        repeated_symbols,
        kek(),
    )
