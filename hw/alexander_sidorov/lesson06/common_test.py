from typing import Callable
from typing import Sequence
from typing import TypeVar
from typing import Union

from .common import name
from .common import validate_args_types

T = TypeVar("T")


@validate_args_types
def func(arg: Callable) -> None:
    assert arg


def test_validator() -> None:
    func(func)


def test_name() -> None:
    assert name(Union) == "Union"
    assert name(Sequence) == "Sequence"
    assert name(list) == "list"
    assert name([]) == "[]"
    assert name(T) == "T"
