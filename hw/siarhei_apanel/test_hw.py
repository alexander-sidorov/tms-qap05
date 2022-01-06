from datetime import date

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


def test_example() -> None:
    yers = {"a": date(2000, 7, 12), "b": date(2000, 7, 12)}
    dic = {1: 100, 2: 100, 3: 300}
    set1 = {1, 2}
    set2 = {1, 3}
    da = {"a": date(2000, 7, 12), "b": date(1987, 12, 24)}
    dat = date(year=1987, month=8, day=2)
    assert palindrom("") == {"data": True}
    assert palindrom("x") == {"data": True}
    assert palindrom("xx") == {"data": True}
    assert palindrom("xy") == {"data": False}
    assert palindrom(1) == {"errors": ["TypeError"]}
    assert proizvedenie(1, 2, 3) == {"data": 6}
    assert proizvedenie(1) == {"data": 1}
    assert proizvedenie(1, 2) == {"data": 2}
    assert proizvedenie("1", 3) == {"data": "111"}
    assert dateday(dat) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert happybithday(da) == {"data": "b"}
    assert happybithday(yers) == {"errors": ["EqualError"]}
    assert repeat([(), "", "", 1]) == {"data": {"": 2}}
    assert repeat({5: 2, 4: 2, 6: 1, 3: 2}) == {"errors": ["NoRepeatError"]}
    assert repeat({(), "", "", 1}) == {"errors": ["NoRepeatError"]}
    assert repeat("aaabbc") == {"data": {"a": 3, "b": 2}}
    assert html_str("x=1&x=2&y=3") == {"data": {"x": ["1", "2"], "y": ["3"]}}
    assert html_str("a=x&b=y&z=") == {
        "data": {"a": ["x"], "b": ["y"], "z": [""]}
    }
    assert decodding("a3b2c1") == {"data": "aaabbc"}
    assert decodding("a3b2c") == {"errors": ["NoQualityLetterError"]}
    assert codding("aaabb") == {"data": "a3b2"}
    assert rever_dict(dic) == {"data": {100: [1, 2], 300: 3}}
    assert rever_dict({"a": "a", "b": "b"}) == {"data": {"a": "a", "b": "b"}}
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
    assert new_set({1}, {1, 2})["data"]["a in b"] is True
    assert new_set({1}, {1, 2})["data"]["b in a"] is False
    assert diction(1, 2) == {"data": {1: 2}}
    assert diction(1, 2, 3) == {"errors": ["NoPares"]}
    assert diction({1}, 2) == {"errors": ["TypeError"]}
    assert diction([1], 2) == {"errors": ["TypeError"]}
    assert diction(1, 2, {}, 4) == {"errors": ["TypeError"]}
