from functools import wraps
from typing import Any
from typing import Callable
from typing import Hashable
from typing import Iterable
from typing import Literal
from typing import Sequence
from typing import Union

from typing_extensions import ParamSpec

AnySet = Union[set, frozenset]
ErrorsList = list[str]
Errors = dict[Literal["errors"], ErrorsList]
Result = dict[Literal["data", "errors"], Any]
Multiplicative = Union[Sequence, int, float, complex]
Params = ParamSpec("Params")


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
    expected_errors: Union[Iterable[str], UndefinedType] = Undefined,
) -> None:
    """
    Does a full validation of function call.
    Function is called using positional args.
    The result is expected to be a dict.
    Either "data" or "errors" keys must be present in this dict.
    """

    assert (expected_data is Undefined) ^ (expected_errors is Undefined)

    result = func(*args)

    assert isinstance(result, dict)
    assert len(result) == 1

    assert ("errors" in result) or ("data" in result)

    if expected_data is not Undefined:
        assert "errors" not in result
        assert "data" in result

        got = result["data"]
        assert got == expected_data

    if expected_errors is not Undefined:
        assert isinstance(expected_errors, Iterable)
        assert "errors" in result
        assert "data" not in result

        errors: ErrorsList = result["errors"]
        assert isinstance(errors, list)
        assert errors
        for _i, error in enumerate(errors):
            assert isinstance(error, str)
        missing_errors = set(expected_errors) - set(errors)

        _e = (
            f"(unhappy path)\n"
            f" expected errors: {sorted(expected_errors)}\n"
            f" errors:          {sorted(errors)}\n"
            f" missing errors:  {sorted(missing_errors)}\n"
        )
        assert not missing_errors, _e

        _e = f"(unhappy path)\nerrors are not sorted\n{sorted(errors)}"
        assert errors == sorted(errors)


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


def api(func: Callable[Params, Any]) -> Callable[Params, Result]:
    @wraps(func)
    def new_func(*args: Params.args, **kwargs: Params.kwargs) -> Result:
        result = func(*args, **kwargs)
        if isinstance(result, dict) and "errors" in result:
            return result
        return {"data": result}

    return new_func
