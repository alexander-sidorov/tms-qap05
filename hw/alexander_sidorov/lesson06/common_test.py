from typing import Any
from typing import Callable
from typing import Generic
from typing import Literal
from typing import NewType
from typing import Sequence
from typing import TypeVar
from typing import Union

import pytest

from .common import name
from .common import typecheck
from .common import typecheck_arg_callable
from .common import typecheck_arg_special_form
from .common import typecheck_arg_strict_type

T1 = TypeVar("T1")
T2 = NewType("T2", int)


class T3(Generic[T1]):
    pass


def test_typecheck_invalid_call() -> None:
    @typecheck
    def _func(_arg1: Any, _arg2: Any) -> Any:
        pass  # pragma: no cover

    with pytest.raises(AssertionError) as err:
        _func(*[1])  # pylint: disable=no-value-for-parameter

    assert str(err.value) == "invalid usage of >>> _arg2 <<<"


def test_typecheck_unknown() -> None:
    @typecheck
    def _func(_arg1: T2) -> Any:
        pass  # pragma: no cover

    with pytest.raises(AssertionError) as err:
        _func(1)

    assert str(err.value) == "_arg1=1: type int != T2 (expected)"


def test_typecheck_strict_type() -> None:
    assert typecheck_arg_strict_type("arg", "", list[str]) is False
    assert typecheck_arg_strict_type("arg", "", Any) is False


def test_typecheck_arg_callable() -> None:
    assert typecheck_arg_callable("arg", "", list[str]) is False

    def f() -> None:  # pylint: disable=invalid-name
        pass  # pragma: no cover

    assert typecheck_arg_callable("arg", f, Callable[[], int]) is True

    with pytest.raises(AssertionError) as excinfo:
        typecheck_arg_callable("arg", "", Callable)
    assert str(excinfo.value) == "arg='' is not Callable"


def test_typecheck_arg_special_form() -> None:
    assert typecheck_arg_special_form("arg", "x", Literal["x"]) is True

    with pytest.raises(AssertionError) as excinfo:
        typecheck_arg_special_form("arg", 4, Literal["x"])
    assert str(excinfo.value) == "arg=4, not in Literal['x']"


def test_name() -> None:
    assert name(Union) == "Union"
    assert name(Sequence) == "Sequence"
    assert name(list) == "list"
    assert name([]) == "[]"
    assert name(T1) == "T1"
    assert name(T2) == "T2"
