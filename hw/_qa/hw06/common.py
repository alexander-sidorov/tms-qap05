from secrets import choice
from string import ascii_letters
from typing import Any


def azaza(*args: Any, bs: Any = ()) -> Any:  # pylint: disable=invalid-name
    asda = "".join(choice(ascii_letters) for _ in "x" * 12)
    tyyy = type(asda, tuple(bs), {})
    return tyyy(*args)


def validate_data(result: Any) -> None:
    assert isinstance(result, dict), f"{result=!r} is not a dict"
    assert len(result) == 1, "only one key is allowed in result"
    assert "data" in result, "'data' must be in result"


def validate_errors(result: Any) -> None:
    assert isinstance(result, dict), f"{result=!r} is not a dict"
    assert len(result) == 1, "only one key is allowed in result"
    assert "errors" in result, "'errors' MUST be in result"

    errors = result["errors"]
    assert errors, "errors cannot be empty"
    assert isinstance(errors, list), "errors must be a list of str"
    assert errors == sorted(errors), "errors must be sorted"
    for i, error in enumerate(errors):
        err = f"errors[{i}] = {error!r} - must be a str"
        assert isinstance(error, str), err


def qual_name(func: Any) -> str:
    return ".".join(
        (
            func.__module__,
            func.__name__,
        )
    )
