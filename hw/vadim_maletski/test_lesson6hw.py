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
    assert (level_01("")) == {"data": True}
    assert (level_01("xx")) == {"data": True}
    assert (level_01("xy")) == {"data": False}
    assert (level_02()) == {"errors": ["argument must not be empty"]}
    assert (level_02(2, [2], 2, [2])) == {
        "errors": "types arguments=(2, [2], 2, [2]) must be not multiplied"
    }
    assert (level_02(1, 2, 3)) == {"data": 6}
    assert (level_02("a" * 2)) == {"data": "aa"}
    assert (level_02(())) == {"data": ()}
    assert (level_02((2,), 2)) == {"data": (2, 2)}
    assert (level_02("")) == {"data": ""}
    assert (level_02("a", 2)) == {"data": "aa"}
    assert (level_02((1, 2))) == {"data": (1, 2)}
    assert (level_03(date(year=2222, month=8, day=2))) == {
        "data": {"year": 2222, "month": 8, "day": 2, "age": None}
    }
    assert (level_03(date(year=1987, month=8, day=2))) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert (level_03(...)) == {"errors": ["type must be date"]}
    assert (level_03(None)) == {"errors": ["type must be date"]}
    assert (level_03(1)) == {"errors": ["type must be date"]}
    assert (level_03(1.0)) == {"errors": ["type must be date"]}
    assert (level_03(1j)) == {"errors": ["type must be date"]}
    assert (level_03(object())) == {"errors": ["type must be date"]}
    assert (level_03(object)) == {"errors": ["type must be date"]}
    assert (level_03(type("_", (), {}))) == {"errors": ["type must be date"]}
    assert (level_03(type)) == {"errors": ["type must be date"]}
    assert (level_03(level_03)) == {"errors": ["type must be date"]}
    assert (level_03([[], []])) == {"errors": ["type must be date"]}
    assert (
        level_04({"A": date(2000, 1, 1), "B": date(1999, 1, 1)})
    ) == {  # noqa: JS101
        "data": "B"
    }
    assert level_04(
        {1: date(1990, 1, 1), 2: date(1990, 1, 2), 3: date(1950, 1, 1)}
    ) == {"data": 3}
    assert (level_04(...)) == {"errors": ["argument must be dict"]}
    assert (level_04(None)) == {"errors": ["argument must be dict"]}
    assert (level_04(1)) == {"errors": ["argument must be dict"]}
    assert (level_04(1.0)) == {"errors": ["argument must be dict"]}
    assert (level_04(1j)) == {"errors": ["argument must be dict"]}
    assert (level_04(object())) == {"errors": ["argument must be dict"]}
    assert (level_04(object)) == {"errors": ["argument must be dict"]}
    assert (level_04(type("_", (), {}))) == {  # noqa: JS101
        "errors": ["argument must be dict"]
    }
    assert (level_04(type)) == {"errors": ["argument must be dict"]}
    assert (level_04(level_04)) == {"errors": ["argument must be dict"]}
    assert (level_04(date(1999, 1, 1))) == {
        "errors": ["argument must be dict"]
    }
    assert (level_04([[], []])) == {"errors": ["argument must be dict"]}
    assert (level_05([])) == {"data": {}}
    assert (level_05({})) == {"data": {}}
    assert (level_05([(), "", "", 1])) == {"data": {"": 2}}
    assert (level_05(((), (), ()))) == {"data": {(): 3}}
    assert (level_05("aaa")) == {"data": {"a": 3}}
    assert (level_05({1, 2, 3})) == {"errors": ["argument must be collection"]}
    assert (level_05((1, 2, 3))) == {"data": {}}
    assert (level_05(...)) == {"errors": ["argument must be collection"]}
    assert (level_05(None)) == {"errors": ["argument must be collection"]}
    assert (level_05(1)) == {"errors": ["argument must be collection"]}
    assert (level_05(1.0)) == {"errors": ["argument must be collection"]}
    assert (level_05(1j)) == {"errors": ["argument must be collection"]}
    assert (level_05(object())) == {"errors": ["argument must be collection"]}
    assert (level_05(object)) == {"errors": ["argument must be collection"]}
    assert (level_05(type("_", (), {}))) == {  # noqa: JS101
        "errors": ["argument must be collection"]
    }
    assert (level_05(type)) == {"errors": ["argument must be collection"]}
    assert (level_05(level_05)) == {"errors": ["argument must be collection"]}
    assert (level_05(date(1999, 1, 1))) == {
        "errors": ["argument must be collection"]
    }
    assert (level_05([[], []])) == {"errors": "unhashable type"}
    assert (level_06(9)) == {"errors": ["argument must be string"]}
    assert (level_06("x=1&x=2&y=3")) == {"data": {"x": ["1", "2"], "y": ["3"]}}
    assert (level_06("")) == {"data": {}}
    assert (level_06("value=")) == {"data": {}}
    assert (level_06("ab=cd&ef=gh&ef=ij")) == {
        "data": {"ab": ["cd"], "ef": ["gh", "ij"]}
    }
    assert (level_06(...)) == {"errors": ["argument must be string"]}
    assert (level_06(None)) == {"errors": ["argument must be string"]}
    assert (level_06(1.0)) == {"errors": ["argument must be string"]}
    assert (level_06(1j)) == {"errors": ["argument must be string"]}
    assert (level_06(object())) == {"errors": ["argument must be string"]}
    assert (level_06(object)) == {"errors": ["argument must be string"]}
    assert (level_06(type("_", (), {}))) == {  # noqa: JS101
        "errors": ["argument must be string"]
    }
    assert (level_06(type)) == {"errors": ["argument must be string"]}
    assert (level_06(level_05)) == {"errors": ["argument must be string"]}
    assert (level_06(date(1999, 1, 1))) == {
        "errors": ["argument must be string"]
    }
    assert (level_06([[], []])) == {"errors": ["argument must be string"]}
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
    assert (level_09(None)) == {"errors": ["argument must not be empty"]}
    assert (level_09({1: 100, 2: 100, 3: 300})) == {  # noqa: JS101
        "data": {100: [1, 2], 300: [3]}
    }
    assert (level_09(...)) == {"errors": ["argument must not be empty"]}
    assert (level_09(1)) == {"errors": ["argument must not be empty"]}
    assert (level_09(1.0)) == {"errors": ["argument must not be empty"]}
    assert (level_09(1j)) == {"errors": ["argument must not be empty"]}
    assert (level_09(object())) == {"errors": ["argument must not be empty"]}
    assert (level_09(object)) == {"errors": ["argument must not be empty"]}
    assert (level_09(type("_", (), {}))) == {  # noqa: JS101
        "errors": ["argument must not be empty"]
    }
    assert (level_09(type)) == {"errors": ["argument must not be empty"]}
    assert (level_09(level_05)) == {"errors": ["argument must not be empty"]}
    assert (level_09(date(1999, 1, 1))) == {
        "errors": ["argument must not be empty"]
    }
    assert (level_09([[], []])) == {"errors": ["argument must not be empty"]}

    assert (level_10(None, None)) == {
        "errors": [
            "argument must be list, str or tuple",
            "argument must be list, str or tuple",
        ]
    }
    assert (level_10("abc", [1, 2])) == {"data": {"a": 1, "b": 2, "c": None}}
    assert (level_10("ab", [1, 2, 3])) == {"data": {"a": 1, "b": 2, "...": 3}}
    assert (level_10("ab", "cd")) == {"data": {"a": "c", "b": "d"}}
    assert (level_10("", "")) == {"data": {}}
    assert (level_11(frozenset(), frozenset())) == {
        "data": {
            "a&b": frozenset(),
            "a|b": frozenset(),
            "a-b": frozenset(),
            "b-a": frozenset(),
            "|a-b|": frozenset(),
            "a in b": True,
            "b in a": True,
        }
    }
    assert (level_11(..., ...)) == {
        "errors": ["argument must be set", "argument must be set"]
    }
    assert (level_11(None, ...)) == {
        "errors": ["argument must be set", "argument must be set"]
    }
    assert (level_11(1.0, None)) == {
        "errors": ["argument must be set", "argument must be set"]
    }
    assert (level_11(1j, object)) == {
        "errors": ["argument must be set", "argument must be set"]
    }
    assert (level_11(object(), object())) == {
        "errors": ["argument must be set", "argument must be set"]
    }
    assert (level_11(object, 1j)) == {
        "errors": ["argument must be set", "argument must be set"]
    }
    assert (level_11(type("_", (), {}), "a")) == {  # noqa: JS101
        "errors": ["argument must be set", "argument must be set"]
    }
    assert (level_11(type, [])) == {
        "errors": ["argument must be set", "argument must be set"]
    }
    assert (level_11(level_05, {})) == {  # noqa: JS101
        "errors": ["argument must be set", "argument must be set"]
    }
    assert (level_11(date(1999, 1, 1), {})) == {  # noqa: JS101
        "errors": ["argument must be set", "argument must be set"]
    }
    assert (level_11([[], []], frozenset())) == {
        "errors": ["argument must be set"]
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
    assert (level_12()) == {"errors": ["argument must not be empty"]}
    assert (level_12(1, 2)) == {"data": {1: 2}}
    assert (level_12(1, 2, 3, "a", 5, {}, 6, object)) == {  # noqa: JS101
        "data": {1: 2, 3: "a", 5: {}, 6: object}
    }
