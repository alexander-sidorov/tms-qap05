from typing import Callable

from .common import validate_args_types


@validate_args_types
def func(arg: Callable) -> None:
    assert arg


def test_validator() -> None:
    func(func)
