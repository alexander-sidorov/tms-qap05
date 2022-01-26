from datetime import date

from hw.siarhei_apanel.refakt import DupCounter05
from hw.siarhei_apanel.refakt import HttpQuery03
from hw.siarhei_apanel.refakt import Multiplier04
from hw.siarhei_apanel.refakt import Palindrome01
from hw.siarhei_apanel.refakt import User02
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
    d5 = [1, 1, 1, 1, 2, 2, 3]
    c5 = DupCounter05(d5)
    obj1 = Multiplier04()
    badobj = Multiplier04()
    badobj.add([]).add({}).add({4})
    obj1.add(2).add(3).add(4)
    obj = HttpQuery03("x=1&y=2&y=3")
    objer = HttpQuery03(123)
    yers = {"a": date(2000, 7, 12), "b": date(2000, 7, 12)}
    noyer = {"a": 1998, "b": date(1999, 2, 2)}
    dic = {1: 100, 2: 100, 3: 300}
    dic1 = 123
    c4 = DupCounter05(dic1)
    set1 = {1, 2}
    set2 = {1, 3}
    da = {"a": date(2000, 7, 12), "b": date(1987, 12, 24)}
    dat2 = date(year=1987, month=8, day=2)
    dat = date(year=1987, month=8, day=2)
    nodate = 1998

    assert palindrom("") == {"data": True}
    assert palindrom("x") == {"data": True}
    assert palindrom("xx") == {"data": True}
    assert palindrom("xy") == {"data": False}
    assert "errors" in palindrom(1)
    assert proizvedenie(1, 2, 3) == {"data": 6}
    assert proizvedenie(("",)) == {"data": ""}
    assert proizvedenie(1) == {"data": 1}
    assert proizvedenie(1, 2) == {"data": 2}
    assert proizvedenie("1", 3) == {"data": "111"}
    assert "errors" in proizvedenie("a", "a")
    assert "errors" in proizvedenie(1, {2})
    assert dateday(dat) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert "errors" in dateday(1998)
    assert happybithday(da) == {"data": "b"}
    assert "errors" in happybithday([yers])
    assert "errors" in happybithday(noyer)
    assert repeat([(), "", "", 1]) == {"data": {"": 2}}
    assert repeat({5: 2, 4: 2, 6: 1, 3: 2}) == {"data": {}}
    assert repeat({(), "", "", 1}) == {"data": {}}
    assert repeat("aaabbc") == {"data": {"a": 3, "b": 2}}
    assert repeat([]) == {"data": {}}
    assert "errors" in repeat(1)
    assert html_str("x=1&x=2&y=33") == {"data": {"x": ["1", "2"], "y": ["33"]}}
    assert html_str("a=x&b=y&z=") == {
        "data": {"a": ["x"], "b": ["y"], "z": [""]}
    }
    assert "errors" in html_str([])
    assert html_str("a=x&b=y&z=z") == {
        "data": {"a": ["x"], "b": ["y"], "z": ["z"]}
    }
    assert decodding("a3b2c1") == {"data": "aaabbc"}
    assert decodding("") == {"data": ""}
    assert "errors" in decodding(123)
    assert "errors" in decodding("a3b2c")
    assert "errors" in decodding("1a3b2c2")
    assert codding("aaabb") == {"data": "a3b2"}
    assert "errors" in codding(123)
    assert codding("a") == {"data": "a1"}
    assert codding("aa") == {"data": "a2"}
    assert codding("ab") == {"data": "a1b1"}
    assert codding("") == {"data": ""}
    assert "errors" in codding("ccc%")
    assert rever_dict(dic) == {"data": {100: [1, 2], 300: 3}}
    assert rever_dict({"a": "a", "b": "b"}) == {"data": {"a": "a", "b": "b"}}
    assert "errors" in rever_dict({"a"})
    assert "data" in new_dict(["a", "b", "c"], [1, 2])
    assert "errors" in new_dict(1, {1, 2})
    assert "errors" in new_dict((1, 3, {4}), {1, 2})
    assert new_dict("ab", [1, 2, 3]) == {"data": {"a": 1, "b": 2, ...: [3]}}
    assert new_dict("abс", [1, 2, 3]) == {"data": {"a": 1, "b": 2, "с": 3}}
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
    assert "errors" in new_set({""}, [])
    assert new_set({1}, {1, 2})["data"]["a in b"] is True
    assert new_set({1}, {1, 2})["data"]["b in a"] is False
    assert diction(1, 2) == {"data": {1: 2}}
    assert "errors" in diction(1, 2, 3)
    assert "errors" in diction({1}, 2)
    assert "errors" in diction([1], 2)
    assert "errors" in diction(1, 2, {}, 4)
    assert "errors" in diction("a", "b", set(), "c")
    assert Palindrome01("xyx")
    assert not Palindrome01("xy x")
    assert User02(dat2).age == 34
    assert "errors" in User02(nodate).age
    assert obj["x"] == ["1"]
    assert obj["y"] == ["2", "3"]
    assert obj["z"] is None
    assert "errors" in objer.__getitem__("x")
    assert obj1.get_result() == 24
    assert "errors" in badobj.get_result()
    assert c5.get_dups() == {1: 4, 2: 2}
    assert "errors" in c4.get_dups()
