from datetime import date
from typing import Any
from typing import Callable
from typing import FrozenSet
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
    validate(
        task_05,
        "abc",
        expected_data={},
    )
    validate(
        task_05,
        "aaab",
        expected_data={"a": 3},
    )
    validate(
        task_05,
        {1, 2, 3},
        expected_data={},
    )

    validate(
        task_05,
        [[], []],
        expected_errors=[
            "collection[0]=[] is not hashable",
            "collection[1]=[] is not hashable",
        ],
    )


def test_task_06() -> None:
    validate(
        task_06,
        "",
        expected_data={},
    )
    validate(
        task_06,
        "xx=",
        expected_data={"xx": [""]},
    )
    validate(
        task_06,
        "xx=&yy=",
        expected_data={"xx": [""], "yy": [""]},
    )
    validate(
        task_06,
        "xx=1&yy=2",
        expected_data={"xx": ["1"], "yy": ["2"]},
    )
    validate(
        task_06,
        "xx=1&yy=2&&yy=3",
        expected_data={"xx": ["1"], "yy": ["2", "3"]},
    )


def test_task_07() -> None:
    validate(
        task_07,
        "",
        expected_data="",
    )
    validate(
        task_07,
        "x0",
        expected_data="",
    )
    validate(
        task_07,
        "x1",
        expected_data="x",
    )
    validate(
        task_07,
        "x11",
        expected_data="x" * 11,
    )
    validate(
        task_07,
        "x11y12",
        expected_data="x" * 11 + "y" * 12,
    )

    validate(
        task_07,
        "xx11y12",
        expected_errors=[
            "folded_text='xx11y12' is malformed",
        ],
    )


def test_task_08() -> None:
    validate(
        task_08,
        "",
        expected_data="",
    )
    validate(
        task_08,
        "x",
        expected_data="x1",
    )
    validate(
        task_08,
        "xxxxxxxxxxxy",
        expected_data="x11y1",
    )
    validate(
        task_08,
        "aba",
        expected_data="a1b1a1",
    )

    validate(
        task_08,
        "aba1",
        expected_errors=[
            "integers MUST not be present in flatten text",
        ],
    )


def test_task_09() -> None:
    validate(
        task_09,
        {},
        expected_data={},
    )
    validate(
        task_09,
        {1: 2},
        expected_data={2: 1},
    )
    validate(
        task_09,
        {1: 2, 3: 2},
        expected_data={2: [1, 3]},
    )

    validate(
        task_09,
        {1: {}, 3: []},
        expected_errors=[
            "value=[] of key=3 cannot be used as a new key",
            "value={} of key=1 cannot be used as a new key",
        ],
    )


def test_task_10() -> None:
    validate(
        task_10,
        {},
        [],
        expected_data={},
    )
    validate(
        task_10,
        {1, 2, 3},
        frozenset({1, 2, 3}),
        expected_data={1: 1, 2: 2, 3: 3},
    )
    validate(
        task_10,
        "ab",
        [[], [[]]],
        expected_data={"a": [], "b": [[]]},
    )
    validate(
        task_10,
        "ab",
        "a",
        expected_data={"a": "a", "b": None},
    )
    validate(
        task_10,
        "a",
        "ab",
        expected_data={"a": "a", ...: ["b"]},
    )
    validate(
        task_10,
        [None, None],
        "ab",
        expected_data={None: "b"},
    )
    validate(
        task_10,
        [{}, []],
        "ab",
        expected_errors=[
            "keys[0]={} is not hashable",
            "keys[1]=[] is not hashable",
        ],
    )


def test_task_11() -> None:
    empty: FrozenSet = frozenset()

    validate(
        task_11,
        set(),
        empty,
        expected_data={
            "a&b": empty,
            "a|b": empty,
            "a-b": empty,
            "b-a": empty,
            "|a-b|": empty,
            "a in b": True,
            "b in a": True,
        },
    )

    validate(
        task_11,
        {1, 2, 3},
        {2, 3, 4},
        expected_data={
            "a&b": {2, 3},
            "a|b": {1, 2, 3, 4},
            "a-b": {1},
            "b-a": {4},
            "|a-b|": {1, 4},
            "a in b": False,
            "b in a": False,
        },
    )

    validate(
        task_11,
        {1, 2},
        {1, 2, 3},
        expected_data={
            "a&b": {1, 2},
            "a|b": {1, 2, 3},
            "a-b": empty,
            "b-a": {3},
            "|a-b|": {3},
            "a in b": True,
            "b in a": False,
        },
    )

    validate(
        task_11,
        {1, 2, 3},
        {1, 2},
        expected_data={
            "a&b": {1, 2},
            "a|b": {1, 2, 3},
            "a-b": {3},
            "b-a": empty,
            "|a-b|": {3},
            "a in b": False,
            "b in a": True,
        },
    )


def test_task_12() -> None:
    assert task_12()
