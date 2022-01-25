from datetime import date

from hw.kirill_tobolich.lesson10_hw import DupCounter05
from hw.kirill_tobolich.lesson10_hw import HttpQuery03
from hw.kirill_tobolich.lesson10_hw import Multiplier04
from hw.kirill_tobolich.lesson10_hw import Palindrome
from hw.kirill_tobolich.lesson10_hw import User02


def test_class_palindrome() -> None:
    assert Palindrome("")
    assert Palindrome(" ")
    assert Palindrome("x")
    assert Palindrome("xx")
    assert Palindrome("abccba")
    assert not Palindrome("xy")
    assert not Palindrome(123321)  # type: ignore


def test_class_user02() -> None:
    d1 = date(2020, 1, 23)
    d2 = date(year=1987, month=8, day=2)
    d3 = date(year=1987, month=1, day=2)
    assert User02(d1).age == 2
    assert User02(d2).age == 34
    assert User02(d3).age == 35


def test_class_httpquery03() -> None:
    obj = HttpQuery03("x=1&y=2&y=3")
    assert obj["x"] == ["1"]
    assert obj["y"] == ["2", "3"]
    assert obj["z"] is None


def test_class_multiplier04() -> None:
    obj = Multiplier04()
    obj.add(2).add(3).add(4)
    assert obj.get_result() == 24


def test_class_dupcounter05() -> None:
    l1 = [1, 1, 1, 1, 2, 2, 3]
    c1 = DupCounter05(l1)
    assert c1.get_dups() == {1: 4, 2: 2}
