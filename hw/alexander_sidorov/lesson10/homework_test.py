from datetime import date
from typing import Any

import pytest

from hw.alexander_sidorov.lesson10.homework import DupCounter05
from hw.alexander_sidorov.lesson10.homework import HttpQuery03
from hw.alexander_sidorov.lesson10.homework import Multiplier04
from hw.alexander_sidorov.lesson10.homework import Palindrome01
from hw.alexander_sidorov.lesson10.homework import User02


@pytest.mark.parametrize(
    "arg,expected",
    [
        ["", True],
        ["a", True],
        ["aa", True],
        ["Aa", False],
    ],
)
def test_palindrome_01(arg: str, expected: bool) -> None:
    obj = Palindrome01(arg)
    diff = expected ^ bool(obj)
    assert not diff


today = date.today()


@pytest.mark.parametrize(
    "arg,expected",
    [
        [date(today.year - 10, today.month, today.day), 10],
    ],
)
def test_user_02(arg: date, expected: int) -> None:
    obj = User02(arg)
    assert obj.age == expected


@pytest.mark.parametrize(
    "arg,expected",
    [
        ["", {}],
        ["x=1", {"x": "1"}],
        ["x=1&x=2", {"x": ["1", "2"]}],
        ["x=1&y=2", {"x": "1", "y": "2"}],
    ],
)
def test_http_query_03(arg: str, expected: dict) -> None:
    obj = HttpQuery03(arg)
    for key, expected_value in expected.items():
        assert obj[key] == expected_value


@pytest.mark.parametrize(
    "args,expected",
    [
        [["a", 1, 2, 3], "aaaaaa"],
        [[0, 1, 2], 0],
        [[1, 2, 3, "a"], "aaaaaa"],
        [[1, 2, 3], 6],
    ],
)
def test_multiplier_04(args: list, expected: Any) -> None:
    obj = Multiplier04()
    for arg in args:
        ret = obj.add(arg)
        assert ret is obj
    assert obj.get_result() == expected


@pytest.mark.parametrize(
    "arg,expected",
    [
        ["aaaaaa", {"a": 6}],
        [["a", 1, 2, 3], {}],
        [[1, 1, 1, 1, 2, 2, 3], {1: 4, 2: 2}],
        [{1: 1, 2: 1, 3: 1}, {}],
    ],
)
def test_dup_counter_05(arg: Any, expected: Any) -> None:
    obj = DupCounter05(arg)
    assert obj.get_dups() == expected
