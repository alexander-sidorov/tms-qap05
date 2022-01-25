from secrets import choice
from string import ascii_letters
from typing import Any


def azaza(*args: Any, bs: Any = ()) -> Any:  # pylint: disable=invalid-name
    asda = "".join(choice(ascii_letters) for _ in "x" * 12)
    tyyy = type(asda, tuple(bs), {})
    return tyyy(*args)


def validate_data(result: Any) -> None:
    assert isinstance(result, dict)
    assert len(result) == 1
    assert "data" in result


def validate_errors(result: Any) -> None:
    assert isinstance(result, dict)
    assert len(result) == 1
    assert "errors" in result

    errors = result["errors"]
    assert errors
    assert isinstance(errors, list)
    assert errors == sorted(errors)
    for error in errors:
        assert isinstance(error, str)


def qual_name(func: Any) -> str:
    return ".".join(
        (
            func.__module__,
            func.__name__,
        )
    )
