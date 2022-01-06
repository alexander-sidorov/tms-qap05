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
from hw.vadim_maletski.func6 import level_10a
from hw.vadim_maletski.func6 import level_10b
from hw.vadim_maletski.func6 import level_11
from hw.vadim_maletski.func6 import level_12


def test() -> None:

    assert level_01("xx") == {"data": True}
    assert level_02((1, 2, 3)) == {"data": 6}
    assert level_03(date(year=1987, month=8, day=2)) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert level_04(  # noqa: BLK100
        {
            "A": date(year=2000, month=1, day=1),
            "B": date(year=1999, month=1, day=1),
        }
    ) == {"data": "B"}
    assert level_05([(), "", "", 1]) == {"data": {"": 2}}
    assert level_06("x=1&x=2&y=3") == {"data": {"x": ["1", "2"], "y": ["3"]}}
    assert level_07("a3b2c1") == {"data": "aaabbc"}
    assert level_08("aaabb") == {"data": "a3b2"}
    assert level_09({1: 100, 2: 100, 3: 300}) == {  # noqa: JS101
        "data": {100: [1, 2], 300: [3]}
    }
    assert level_10a("abc", [1, 2]) == {"data": {"a": 1, "b": 2, "c": None}}
    assert level_10b("ab", [1, 2, 3]) == {"data": {"a": 1, "b": 2, "...": 3}}
    assert level_11({1, 2}, {1, 3}) == {  # noqa: JS101
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
    assert level_12((1, 2)) == {"data": {1: 2}}
