from typing import Any
from typing import Callable
from typing import Generic
from typing import Literal
from typing import Sequence
from typing import TypeVar
from typing import Union

import pytest

from .common import name
from .common import validate_args_types

T = TypeVar("T")


@validate_args_types
def func_c(arg: Callable) -> None:
    assert arg


@validate_args_types
def func_any(arg: Any) -> None:
    assert arg


@validate_args_types
def func_t(arg: T) -> None:
    assert arg


class G(Generic[T]):
    pass


@validate_args_types
def func_g(arg: G[int]) -> None:
    assert arg


@validate_args_types
def func_lc(arg: list[Callable]) -> list:
    return arg[:]


@validate_args_types
def func_lit(_arg: Literal[420]) -> None:
    pass


@pytest.mark.parametrize(
    "func,arg,ok",
    [
        pytest.param(func_any, ..., True, id="any"),
        pytest.param(func_c, ..., False, id="callable-fail"),
        pytest.param(func_c, func_c, True, id="callable-ok"),
        pytest.param(func_g, ..., False, id="generic-false"),
        pytest.param(func_g, G(), True, id="generic-true"),
        pytest.param(func_lc, [], True, id="list-callable-ok"),
        pytest.param(func_lit, ..., False, id="literal-fail"),
        pytest.param(func_lit, 420, True, id="literal-ok"),
        pytest.param(func_t, ..., True, id="typevar"),
    ],
)
def test_validator(func: Callable, arg: Any, ok: bool) -> None:
    if not ok:
        with pytest.raises(AssertionError):
            func(arg)
    else:
        func(arg)


def test_name() -> None:
    assert name(Union) == "Union"
    assert name(Sequence) == "Sequence"
    assert name(list) == "list"
    assert name([]) == "[]"
    assert name(T) == "T"
