from datetime import date

from hw.vadim_maletski.func6 import level_01
from hw.vadim_maletski.func6 import level_02
from hw.vadim_maletski.func6 import level_03
from hw.vadim_maletski.func6 import level_04
from hw.vadim_maletski.func6 import level_05
from hw.vadim_maletski.func6 import level_06
from hw.vadim_maletski.func6 import level_07
from hw.vadim_maletski.func6 import level_08
from hw.vadim_maletski.func6 import level_09
from hw.vadim_maletski.func6 import level_10
from hw.vadim_maletski.func6 import level_11
from hw.vadim_maletski.func6 import level_12


def test() -> None:
    assert (level_01(98)) == {"errors": ["argument must be string"]}
    assert (level_01({"abc"})) == {"errors": ["argument must be string"]}
    assert (level_01("")) == {"data": True}
    assert (level_01("xx")) == {"data": True}
    assert (level_01("xy")) == {"data": False}
    assert (level_02()) == {"errors": ["argument must not be empty"]}
    assert (level_02(1, 2, 3)) == {"data": 6}
    assert (level_02("a" * 2)) == {"data": "aa"}
    assert (level_02(())) == {"data": ()}
    assert (level_02((2,), 2)) == {"data": (2, 2)}
    assert (level_02("")) == {"data": ""}
    assert (level_02("a", 2)) == {"data": "aa"}
    assert (level_02((1, 2))) == {"data": (1, 2)}
    assert (level_03(date(year=2222, month=8, day=2))) == {
        "errors": ["wrong year"]
    }
    assert (level_03(date(year=1987, month=8, day=2))) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert (
        level_04(
            {
                "A": date(year=2000, month=1, day=1),
                "B": date(year=2000, month=1, day=1),
            }
        )
    ) == {"errors": ["years must be a different"]}
    assert (
        level_04(
            {
                "A": date(year=2000, month=1, day=1),
                "B": date(year=1999, month=1, day=1),
            }
        )
    ) == {"data": "B"}
    assert (
        level_04(
            {
                "A": date(year=1999, month=1, day=1),
                "B": date(year=2000, month=1, day=1),
            }
        )
    ) == {"data": "A"}
    assert (level_05([])) == {"data": {}}
    assert (level_05({})) == {"data": {}}
    assert (level_05(True)) == {"errors": ["argument must not be bool"]}
    assert (level_05(False)) == {"errors": ["argument must not be bool"]}
    assert (level_05([(), "", "", 1])) == {"data": {"": 2}}
    assert (level_05(((), (), ()))) == {"data": {(): 3}}
    assert (level_05("aaa")) == {"data": {"a": 3}}
    assert (level_05({1, 2, 3})) == {"data": {}}
    assert (level_05((1, 2, 3))) == {"data": {}}
    assert (level_06(9)) == {"errors": ["argument (query=9) must be string"]}
    assert (level_06("x=1&x=2&y=3")) == {"data": {"x": ["1", "2"], "y": ["3"]}}
    assert (level_06("")) == {"data": {}}
    assert (level_06("value=")) == {"data": {}}
    assert (level_06("ab=cd&ef=gh&ef=ij")) == {
        "data": {"ab": ["cd"], "ef": ["gh", "ij"]}
    }
    assert (level_07(9)) == {"errors": ["argument (string=9) must be string"]}
    assert (level_07("a3b2c1")) == {"data": "aaabbc"}
    assert (level_07("a10b1")) == {"data": "aaaaaaaaaab"}
    assert (level_08(9)) == {"errors": ["argument (string=9) must be string"]}
    assert (level_08("aaabb")) == {"data": "a3b2"}
    assert (level_08("aaabbab")) == {"data": "a3b2a1b1"}
    assert (level_09(None)) == {"errors": ["argument must not be empty"]}
    assert (level_09({1: 100, 2: 100, 3: 300})) == {  # noqa: JS101
        "data": {100: [1, 2], 300: [3]}
    }
    assert (level_10(None, None, None, None)) == {
        "errors": [
            "arguments (a1=None) must not be empty",
            "arguments (b1=None) must not be empty",
            "arguments (a2=None) must not be empty",
            "arguments (b2=None) must not be empty",
        ]
    }
    assert (level_10("ab", [1, 2, 3], "abc", [1, 2])) == {
        "data": ({"a": 1, "b": 2, None: 3}, {"a": 1, "b": 2, "c": "..."})
    }
    assert (level_11("{}", "{}")) == {
        "errors": [
            "argument s1='{}' must be set",
            "argument s2='{}' must be set",
        ]
    }
    assert (level_11({1, 2}, {1, 3})) == {  # noqa: JS101
        "data": {
            "a&b": {1},
            "a|b": {1, 2, 3},
            "a-b": {2},
            "b-a": {3},
            "|a-b|": {2, 3},
            "a in b": False,
            "b in a": False,
        }
    }
    assert (level_11({1, 2}, {1, 2, 3})) == {  # noqa: JS101
        "data": {
            "a&b": {1, 2},
            "a|b": {1, 2, 3},
            "a-b": set(),
            "b-a": {3},
            "|a-b|": {3},
            "a in b": True,
            "b in a": False,
        }
    }
    assert (level_12(())) == {"errors": ["argument must not be empty"]}
    assert (level_12((1, 2))) == {"data": {1: 2}}
