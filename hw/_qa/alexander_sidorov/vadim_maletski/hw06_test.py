from secrets import choice
from string import ascii_letters
from typing import Any
from typing import Callable

from hw.vadim_maletski.func6 import level_02
from hw.vadim_maletski.func6 import level_05
from hw.vadim_maletski.func6 import level_06
from hw.vadim_maletski.func6 import level_07
from hw.vadim_maletski.func6 import level_08
from hw.vadim_maletski.func6 import level_09
from hw.vadim_maletski.func6 import level_10
from hw.vadim_maletski.func6 import level_12


class UndefinedType:
    pass


Undefined = UndefinedType()


def lol() -> Any:
    name = "".join(choice(ascii_letters) for _ in range(24))
    typ = type(name, (), {})
    return typ()


def validate(
    func: Callable,
    *args: Any,
    xdata: Any = Undefined,
    xerrors: bool = False,
) -> None:
    result = func(*args)

    if xerrors:
        errors = result.get("errors")
        assert errors
        assert isinstance(errors, list)
        for error in errors:
            assert isinstance(error, str)
        assert errors == sorted(errors)
        return

    if xdata is not Undefined:
        errors = result.get("errors")
        assert not errors

        data = result.get("data", Undefined)
        assert data is not Undefined, f"no key 'data' in {result=!r}"
        assert data == xdata


def test_task_02() -> None:
    validate(
        level_02,
        2,
        "a",
        2,
        xdata="aaaa",
    )

    validate(
        level_02,
        "a",
        2,
        "a",
        xerrors=True,
    )


def test_task_05() -> None:
    validate(
        level_05,
        "aa",
        xdata={"a": 2},
    )

    validate(
        level_05,
        {1: 2, 2: 2},
        xdata={},
    )

    validate(
        level_05,
        {1, 2},
        xdata={},
    )

    validate(
        level_05,
        [[], [], {}, {}],
        xerrors=True,
    )


def test_task_06() -> None:
    validate(
        level_06,
        "",
        xdata={},
    )
    validate(
        level_06,
        "xx=&yy=",
        xdata={"xx": [""], "yy": [""]},
    )

    validate(
        level_06,
        lol(),
        xerrors=True,
    )


def test_task_07() -> None:
    validate(
        level_07,
        "",
        xdata="",
    )
    validate(
        level_07,
        "a1",
        xdata="a",
    )
    validate(
        level_07,
        "a11",
        xdata="a" * 11,
    )
    validate(
        level_07,
        "a11b1",
        xdata="a" * 11 + "b",
    )
    validate(
        level_07,
        "a1b1a1",
        xdata="aba",
    )

    validate(
        level_07,
        "a",
        xerrors=True,
    )
    validate(
        level_07,
        "aaa1",
        xerrors=True,
    )
    validate(
        level_07,
        "1a",
        xerrors=True,
    )


def test_task_08() -> None:
    validate(
        level_08,
        "",
        xdata="",
    )
    validate(
        level_08,
        "a",
        xdata="a1",
    )
    validate(
        level_08,
        "aaabb",
        xdata="a3b2",
    )
    validate(
        level_08,
        "aaabba",
        xdata="a3b2a1",
    )
    validate(
        level_08,
        "aaaaaaaaaaabba",
        xdata="a11b2a1",
    )

    validate(
        level_08,
        "a2b2a1",
        xerrors=True,
    )


def test_task_09() -> None:
    validate(
        level_09,
        {1: 100, 2: 100, 3: 300},
        xdata={100: [1, 2], 300: 3},
    )

    validate(
        level_09,
        {1: [], 2: {}, 3: [], 4: set()},
        xerrors=True,
    )


def test_task_10() -> None:
    validate(
        level_10,
        "1234",
        "ab",
        xdata={"1": "a", "2": "b", "3": None, "4": None},
    )

    validate(
        level_10,
        "ab",
        "1234",
        xdata={"a": "1", "b": "2", ...: ["3", "4"]},
    )

    validate(
        level_10,
        [[]],
        "a",
        xerrors=True,
    )


def test_level_12() -> None:
    validate(
        level_12,
        *(1, 2, 3, 4),
        xdata={1: 2, 3: 4},
    )

    validate(
        level_12,
        xdata={},
    )

    validate(
        level_12,
        *(1, 2, 3),
        xerrors=True,
    )

    validate(
        level_12,
        *([], 1, {}, 2, set(), 3),
        xerrors=True,
    )
