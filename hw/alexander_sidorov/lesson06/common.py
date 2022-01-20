from functools import wraps
from typing import Any
from typing import Callable
from typing import Collection
from typing import Hashable
from typing import Iterable
from typing import Literal
from typing import Sequence
from typing import TypeVar
from typing import Union
from typing import get_args
from typing import get_origin

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

        assert errors == sorted(errors)


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


T1 = TypeVar("T1")


def validate_args_types(func: Callable[Params, T1]) -> Callable[Params, T1]:
    @wraps(func)
    def decorated(*args: Params.args, **kwargs: Params.kwargs) -> T1:
        assert not kwargs

        annotations = (
            (p, t)
            for (p, t) in func.__annotations__.items()
            if p not in {"return"}
        )
        pos_annos = (
            next(annotations) for _ in "_" * func.__code__.co_argcount
        )

        arguments = iter(args)  # type: ignore

        for param, exp_type in pos_annos:
            arg = next(arguments)
            _validate_arg_type(arg, exp_type, param)

        if star_annos := list(annotations):
            star_name, star_type = star_annos[0]
            for i, arg in enumerate(arguments):
                _validate_arg_type(arg, star_type, f"*{star_name}[{i}]")

        return func(*args, **kwargs)

    return decorated


def _validate_arg_type(  # noqa: CCR001 # 21!
    arg: Any,
    exp_type: Any,
    param: str,
) -> None:
    if exp_type is Any or isinstance(exp_type, TypeVar):
        return

    exp_type_ = name(exp_type)

    exp_origin = get_origin(exp_type)
    exp_origin_ = name(exp_origin)
    exp_args = get_args(exp_type)

    type_arg = type(arg)
    type_arg_ = name(type_arg)

    if exp_origin is None:
        err = f"{param}={arg!r}, {type_arg_} != expected: {exp_type_}"
        assert isinstance(arg, exp_type), err

    elif exp_origin is Union:
        exp_args_ = ", ".join(sorted(name(t) for t in exp_args))
        err = f"{param}={arg!r}, {type_arg_} != expected: Union[{exp_args_}]"
        assert isinstance(arg, exp_args), err

    elif issubclass(exp_origin, Collection):
        err = f"{param}={arg!r}, {type_arg_} != expected: {exp_origin_}"
        assert isinstance(arg, exp_origin), err
        if issubclass(exp_origin, dict):
            for key, value in arg.items():
                _validate_arg_type(key, exp_args[0], f"{param} key")
                _validate_arg_type(value, exp_args[1], f"{param}[{key!r}]")


def name(obj: Any) -> str:
    if name := getattr(obj, "__name__", None):
        assert name
        return str(name)
    if name := getattr(obj, "_name", None):
        return str(name)
    return repr(obj)
