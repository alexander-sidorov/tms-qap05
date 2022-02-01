import inspect
from functools import wraps
from numbers import Number
from types import FunctionType
from typing import Any
from typing import Callable
from typing import Collection
from typing import Hashable
from typing import Iterable
from typing import Literal
from typing import NewType
from typing import Sequence
from typing import TypeVar
from typing import Union
from typing import _SpecialForm
from typing import cast
from typing import get_args
from typing import get_origin

from typing_extensions import ParamSpec


class UndefinedType:
    pass


class CheckState(RuntimeError):
    pass


class WontCheck(CheckState):
    pass


class Approves(CheckState):
    pass


AnySet = Union[set, frozenset]
ErrorsList = list[str]
Errors = dict[Literal["errors"], ErrorsList]
Multiplicative = Union[Sequence, Number]
Params = ParamSpec("Params")
Result = dict[Literal["data", "errors"], Any]
T1 = TypeVar("T1")

Undefined = UndefinedType()


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
        err = "happy path requires 'data' to be in result"
        assert "errors" not in result, err

        err = "happy path requires 'errors' not to be in result"
        assert "data" in result, err

        got = result["data"]
        assert got == expected_data

    if expected_errors is not Undefined:
        assert isinstance(expected_errors, Iterable)

        err = "unhappy path requires 'errors' to be in result"
        assert "errors" in result, err

        err = "unhappy path requires 'data' not to be in result"
        assert "data" not in result, err

        errors: ErrorsList = result["errors"]

        err = f"{errors=!r}: not a list"
        assert isinstance(errors, list), err
        assert errors, "unhappy path requires non-empty errors"

        for i, error in enumerate(errors):
            err = f"errors[{i}]={error!r} is not a str"
            assert isinstance(error, str), err

            err = f"errors[{i}]={error!r}: must be descriptive"
            assert error, err

        missing_errors = set(expected_errors) - set(errors)

        err = (
            f"(unhappy path)\n"
            f" expected errors: {sorted(expected_errors)}\n"
            f" errors:          {sorted(errors)}\n"
            f" missing errors:  {sorted(missing_errors)}\n"
        )
        assert not missing_errors, err

        err = "errors are not sorted"
        assert errors == sorted(errors), err


def hashable(arg: Any) -> bool:
    """
    Tells if the given arg is hashable.
    """

    return isinstance(arg, Hashable)


def api(func: Callable[Params, Any]) -> Callable[Params, Result]:
    @wraps(func)
    def decorated(*args: Params.args, **kwargs: Params.kwargs) -> Result:
        try:
            result = func(*args, **kwargs)
            return {"data": result}
        except AssertionError as err:
            return {"errors": [str(err)]}

    return decorated


def typecheck(func: Callable[Params, T1]) -> Callable[Params, T1]:
    """
    Checks arguments types using function annotations.
    """

    @wraps(func)
    def typechecked(*args: Params.args, **kwargs: Params.kwargs) -> T1:
        err = f"{func.__name__}() is intended to accept positional-only args"
        assert not kwargs, err

        arguments = iter(cast(tuple[Any], args))

        signature = inspect.signature(func)
        parameters = iter(signature.parameters.values())
        variative = None

        for param in parameters:
            if not is_positional(param):
                variative = param
                break

            arg = next(arguments)
            typecheck_arg(param.name, arg, param.annotation)

        if variative:
            for i, arg in enumerate(arguments):
                typecheck_arg(
                    f"*{variative.name}[{i}]",
                    arg,
                    variative.annotation,
                )

        return func(*args, **kwargs)

    return typechecked


POSITIONAL_KINDS = {
    inspect.Parameter.POSITIONAL_ONLY,
    inspect.Parameter.POSITIONAL_OR_KEYWORD,
}


def is_positional(parameter: inspect.Parameter) -> bool:
    return parameter.kind in POSITIONAL_KINDS


def typecheck_arg(
    param: str,
    arg: Any,
    expected: Any,
) -> None:
    checks = {
        typecheck_arg_callable,
        typecheck_arg_collection,
        typecheck_arg_special_form,
        typecheck_arg_strict_type,
    }

    approved = False
    for check in checks:
        approved = check(param, arg, expected)
        if approved:
            break

    if not approved:
        err = (
            f"{param}={arg!r}: "
            f"type {name(type(arg))} != {name(expected)} (expected)"
        )
        raise AssertionError(err)


def typecheck_arg_strict_type(
    param: str,
    arg: Any,
    expected: Any,
) -> bool:
    origin = get_origin(expected)
    if origin is not None:
        return False

    if (
        isinstance_(expected, (FunctionType, _SpecialForm, TypeVar))
        or issubclass_(expected, NewType)  # noqa: W503
        or isinstance_(expected, NewType)  # noqa: W503
    ):
        # covers NewType
        return False

    s_arg_type = name(type(arg))
    s_expected = name(expected)
    err = f"{param}={arg!r}, {s_arg_type} != {s_expected} (expected)"
    assert isinstance(arg, expected), err
    return True


def typecheck_arg_callable(
    param: str,
    arg: Any,
    expected: Any,
) -> bool:
    origin = get_origin(expected)
    if origin is None:
        return False

    if not issubclass_(origin, Callable):
        return False

    err = f"{param}={arg!r} is not Callable"
    assert isinstance(arg, Callable), err  # type: ignore
    return True


def typecheck_arg_special_form(
    param: str,
    arg: Any,
    expected: Any,
) -> bool:
    if expected is Any or isinstance(expected, TypeVar):
        return True

    origin = get_origin(expected)
    if origin is Literal:
        args = get_args(expected)
        s_args = ", ".join(map(repr, args))
        err = f"{param}={arg}, not in Literal[{s_args}]"
        assert arg in get_args(expected), err
        return True

    if origin is not Union:
        return False

    args = get_args(expected)
    s_args = ", ".join(sorted(name(t) for t in args))
    s_arg_type = name(type(arg))
    err = f"{param}={arg!r}, {s_arg_type} != expected: Union[{s_args}]"
    assert isinstance(arg, args), err

    return True


def typecheck_arg_collection(
    param: str,
    arg: Any,
    expected: Any,
) -> bool:
    origin = get_origin(expected)
    if not issubclass_(origin, Collection):
        return False

    typecheck_arg(param, arg, origin)

    if issubclass_(origin, dict):
        args = get_args(expected)
        for key, value in arg.items():
            typecheck_arg(f"{param} key", key, args[0])
            typecheck_arg(f"{param}[{key!r}]", value, args[1])

    return True


def name(obj: Any) -> str:
    if _name := getattr(obj, "__name__", None):
        assert _name
        return str(_name)
    if _name := getattr(obj, "_name", None):
        return str(_name)
    return repr(obj)


def issubclass_(arg1: Any, arg2: Any) -> bool:
    try:
        return issubclass(arg1, arg2)
    except TypeError:
        return False


def isinstance_(arg1: Any, arg2: Any) -> bool:
    try:
        return isinstance(arg1, arg2)
    except TypeError:
        return False
