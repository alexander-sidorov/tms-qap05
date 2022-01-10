from typing import Any
from typing import Callable
from typing import Dict
from typing import FrozenSet
from typing import Hashable
from typing import Iterable
from typing import List
from typing import Set
from typing import Union

AnySet = Union[Set, FrozenSet]
Errors = List[str]
Result = Dict[str, Any]


class UndefinedType:
    pass


Undefined = UndefinedType()


def build_result(
    *,
    data: Any = Undefined,
    errors: Union[Errors, UndefinedType] = Undefined,
) -> Result:
    """
    Composes a Result from given kwargs.
    """

    result: Result = {}

    if errors and errors is not Undefined:
        assert isinstance(errors, list)
        result["errors"] = sorted(errors)

    if not result and data is not Undefined:
        result["data"] = data

    return result


def even(arg: int) -> bool:
    """
    Tells if the given arg number is even.
    """

    return arg % 2 == 0


def validate(
    func: Callable,
    *args: Any,
    expected_data: Any = Undefined,
    expected_errors: Union[Errors, UndefinedType] = Undefined,
) -> None:
    """
    Does a full validation of function call.
    Function is called using positional args.
    The result is expected to be a dict.
    Either "data" or "errors" keys must be present in this dict.
    """

    _e = "double expectations are not allowed"
    assert (expected_data is Undefined) ^ (expected_errors is Undefined), _e

    result = func(*args)

    assert isinstance(result, dict), f"{type(result)=!r}, MUST be a dict"
    assert len(result) == 1, "only one dict key is allowed"

    _e = f"unknown key: {sorted(result)}"
    assert ("errors" in result) or ("data" in result), _e

    if expected_data is not Undefined:
        _e = f"happy path: 'errors' key MUST not be present: {result!r}"
        assert "errors" not in result, _e

        _e = f"happy path: 'data' key MUST be present: {result!r}"
        assert "data" in result, _e

        got = result["data"]
        _e = (
            f"expectations failed for {func.__name__}{args}:\n"
            f"{got=!r} != expected={expected_data!r}"
        )
        assert got == expected_data, _e

    if expected_errors is not Undefined:
        assert isinstance(expected_errors, Iterable)

        _e = f"unhappy path: 'errors' key MUST be present: {result!r}"
        assert "errors" in result, _e

        _e = f"unhappy path: 'data' key MUST not be present: {result!r}"
        assert "data" not in result, _e

        errors: List[str] = result["errors"]
        _e = f"{type(result['errors'])=!r}, MUST be a list"
        assert isinstance(errors, list)

        _e = f"{result['errors']=!r} MUST contain at least one error"
        assert errors, _e

        for i, error in enumerate(errors):
            _e = f"result['errors'][{i}]={error!r}, MUST be a str"
            assert isinstance(error, str), _e

        missing_errors = set(expected_errors) - set(errors)
        _e = f"errors={sorted(errors)}, missing: {sorted(missing_errors)}"
        assert not missing_errors, _e

        assert errors == sorted(errors), "errors are not sorted"


def multiplicative(arg: Any) -> bool:
    """
    Tells if the given arg supports multiplication.
    """

    return hasattr(arg, "__mul__")


def hashable(arg: Any) -> bool:
    """
    Tells if the given arg is hashable.
    """

    return isinstance(arg, Hashable)
