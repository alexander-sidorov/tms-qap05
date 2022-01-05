from datetime import date
from typing import Any  # noqa F401

from hw.siarhei_apanel.refakt import codding
from hw.siarhei_apanel.refakt import dateday
from hw.siarhei_apanel.refakt import decodding
from hw.siarhei_apanel.refakt import diction
from hw.siarhei_apanel.refakt import happybithday
from hw.siarhei_apanel.refakt import html_str
from hw.siarhei_apanel.refakt import new_dict
from hw.siarhei_apanel.refakt import new_set
from hw.siarhei_apanel.refakt import palindrom
from hw.siarhei_apanel.refakt import proizvedenie
from hw.siarhei_apanel.refakt import repeat
from hw.siarhei_apanel.refakt import rever_dict


def test_example() -> None:  # noqa: W503
    yers = {"a": date(2000, 7, 12), "b": date(2000, 7, 12)}  # noqa: E501
    dic = {1: 100, 2: 100, 3: 300}  # noqa: E501
    set1 = {1, 2}
    set2 = {1, 3}
    da = {"a": date(2000, 7, 12), "b": date(1987, 12, 24)}  # noqa: E501
    assert palindrom("") == {"data": True}
    assert palindrom("x") == {"data": True}
    assert palindrom("xx") == {"data": True}
    assert palindrom("xy") == {"data": False}
    # assert palindrom(1) == {"errors": ["TypeError"]} # noqa: E800, E501
    assert proizvedenie(1, 2, 3) == {"data": 6}
    assert proizvedenie(1) == {"data": 1}
    assert proizvedenie(1, 2) == {"data": 2}
    # assert proizvedenie("1", 3) == {"data": "111"} # noqa: E800, E501
    # assert proizvedenie("1", "3") == {"errors": ["TypeError"]} # noqa: E800, E501
    # assert proizvedenie(2, [3]) == {"data": [3, 3]} # noqa: E800, E501
    # assert proizvedenie((1, 3), [9], 2) == {"errors": ["TypeError"]} # noqa: E800, E501
    assert dateday(1993, 7, 12) == {
        "data": {"year": 1993, "month": 7, "day": 12, "age": 28}
    }
    assert dateday(0, 13, -1) == {"errors": ["ValueError"]}
    # assert dateday("0", [13], (-1, 2)) == {"errors": ["TypeError"]} # noqa: E800, E501
    assert happybithday(da) == {"data": "b"}
    assert happybithday(yers) == {"errors": ["EqualError"]}
    assert repeat([(), "", "", 1]) == {"data": {"": 2}}
    assert repeat({5: 2, 4: 2, 6: 1, 3: 2}) == {"data": {2: 3}}
    assert repeat({(), "", "", 1}) == {"errors": ["NoRepeatError"]}
    assert html_str("x=1&x=2&y=3") == {"data": {"x": ["1", "2"], "y": ["3"]}}
    assert decodding("a3b2c1") == {"data": "aaabbc"}
    assert decodding("a3b2c") == {"errors": ["NoQualityLetterError"]}
    # assert decodding(1234) == {"errors": ["TypeError"]} # noqa: E800
    assert codding("aaabb") == {"data": "a3b2"}
    # assert codding(55) == {"errors": ["TypeError"]} # noqa: E800
    assert rever_dict(dic) == {"data": {100: [1, 2], 300: 3}}
    # assert rever_dict([2, 5, 7]) == {"errors": ["TypeError"]} # noqa: E800
    assert new_dict("abc", [1, 2]) == {"data": {"a": 1, "b": 2, "c": None}}
    assert new_dict("ab", [1, 2, 3]) == {"data": {"a": 1, "b": 2, ...: [3]}}
    assert new_set(set1, set2) == {
        "data": {
            "a&b": {1},
            "a|b": {1, 2, 3},
            "a-b": {2},
            "b-a": {3},
            "|a-b|": {2, 3},
            "a in b": False,
            "b in a": False,
        }
    }  # noqa: E501
    assert diction(1, 2) == {"data": {1: 2}}
    assert diction(1, 2, 3) == {"errors": ["NoPares"]}
    assert diction({1}, 2) == {"errors": ["TypeError"]}
    assert diction([1], 2) == {"errors": ["TypeError"]}
    assert diction(1, 2, {}, 4) == {"errors": ["TypeError"]}
