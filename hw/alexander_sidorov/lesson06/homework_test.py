from datetime import date
from typing import Any
from typing import Callable
from typing import Iterable
from typing import List
from typing import Union

from freezegun import freeze_time

from hw.alexander_sidorov.lesson06.homework import task_01
from hw.alexander_sidorov.lesson06.homework import task_02
from hw.alexander_sidorov.lesson06.homework import task_03
from hw.alexander_sidorov.lesson06.homework import task_04
from hw.alexander_sidorov.lesson06.homework import task_05
from hw.alexander_sidorov.lesson06.homework import task_06
from hw.alexander_sidorov.lesson06.homework import task_07
from hw.alexander_sidorov.lesson06.homework import task_08
from hw.alexander_sidorov.lesson06.homework import task_09
from hw.alexander_sidorov.lesson06.homework import task_10
from hw.alexander_sidorov.lesson06.homework import task_11
from hw.alexander_sidorov.lesson06.homework import task_12

Undefined = object()


def validate(
    func: Callable,
    *args: Any,
    expected_data: Any = Undefined,
    expected_errors: Union[List[str], object] = Undefined,
) -> None:
    _e = "double expectations are not allowed"
    assert (expected_data is Undefined) ^ (expected_errors is Undefined), _e

    result = func(*args)

    assert isinstance(result, dict), f"{type(result)=!r}, MUST be a dict"
    assert len(result) == 1, "only one dict key is allowed"
    _e = f"unknown key {result.keys()}"
    assert ("errors" in result) or ("data" in result), _e

    if expected_data is not Undefined:
        _e = "errors key MUST not be present for happy way"
        assert "errors" not in result, _e

        _e = "data key MUST be present for happy path"
        assert "data" in result, _e

        got_data = result["data"]
        _e = f"expectations failed for {func.__name__}{args}"
        assert got_data == expected_data, _e

    if expected_errors is not Undefined:
        assert isinstance(expected_errors, Iterable)

        _e = "errors key MUST be present for failed path"
        assert "errors" in result, _e

        _e = "data key MUST not be present for failed path"
        assert "data" not in result, _e

        errors: List[str] = result["errors"]
        _e = f"{type(result['errors'])=!r}, MUST be a list"
        assert isinstance(errors, list)

        _e = f"{result['errors']=!r} MUST contain at least one error"
        assert errors, _e

        for i, error in enumerate(errors):
            _e = f"{result['errors'][i]=!r} MUST be a str"
            assert isinstance(error, str), _e

        missing_errors = set(expected_errors) - set(errors)
        _e = f"errors={sorted(errors)}, missing: {sorted(missing_errors)}"
        assert not missing_errors, _e

        assert errors == sorted(errors), "errors are not sorted"


def test_task_01() -> None:
    validate(task_01, "", expected_data=True)
    validate(task_01, "x", expected_data=True)
    validate(task_01, "xx", expected_data=True)
    validate(task_01, "xy", expected_data=False)

    validate(
        task_01,
        None,
        expected_errors=["type(arg)=NoneType, MUST be a string"],
    )
    validate(
        task_01,
        1,
        expected_errors=["type(arg)=int, MUST be a string"],
    )


def test_task_02() -> None:
    validate(task_02, "a", 2, expected_data="aa")
    validate(task_02, (3,), 2, expected_data=(3, 3))
    validate(task_02, 0.2, 5, expected_data=1.0)
    validate(task_02, 1j, -1j, expected_data=1)
    validate(task_02, 1, 2, 3, expected_data=6)
    validate(task_02, 1, 2, expected_data=2)
    validate(task_02, 1, expected_data=1)
    validate(task_02, 2, "b", expected_data="bb")
    validate(task_02, 2, "c", 3, expected_data="cccccc")
    validate(task_02, [2], 2, expected_data=[2, 2])
    validate(task_02, True, False, expected_data=0)

    validate(task_02, None, 2, expected_errors=["cannot do: None * 2"])
    validate(task_02, {}, 2, expected_errors=["cannot do: {} * 2"])

    validate(
        task_02,
        2,
        "c",
        3,
        "c",
        expected_errors=["cannot do: 'cccccc' * 'c'"],
    )
    validate(
        task_02,
        expected_errors=["nothing to multiply"],
    )


@freeze_time(date(2000, 1, 1))
def test_task_03() -> None:
    validate(
        task_03,
        date(year=1987, month=8, day=2),
        expected_data={"year": 1987, "month": 8, "day": 2, "age": 12},
    )


def test_task_04() -> None:
    validate(
        task_04,
        {
            1: date(year=1987, month=8, day=2),
            (): date(year=1987, month=8, day=1),
            ...: date(year=1987, month=7, day=1),
        },
        expected_data=...,
    )


def test_task_05() -> None:
    assert task_05()


def test_task_06() -> None:
    assert task_06()


def test_task_07() -> None:
    assert task_07()


def test_task_08() -> None:
    assert task_08()


def test_task_09() -> None:
    assert task_09()


def test_task_10() -> None:
    assert task_10()


def test_task_11() -> None:
    assert task_11()


def test_task_12() -> None:
    assert task_12()
