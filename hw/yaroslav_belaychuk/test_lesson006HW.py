from datetime import date

from hw.yaroslav_belaychuk.lesson006HW import DupCounter05
from hw.yaroslav_belaychuk.lesson006HW import Multiplier04
from hw.yaroslav_belaychuk.lesson006HW import Palindrome01
from hw.yaroslav_belaychuk.lesson006HW import User02
from hw.yaroslav_belaychuk.lesson006HW import date_age
from hw.yaroslav_belaychuk.lesson006HW import palindrom
from hw.yaroslav_belaychuk.lesson006HW import umnogenie
from hw.yaroslav_belaychuk.lesson006HW import zadacha_4
from hw.yaroslav_belaychuk.lesson006HW import zadacha_5
from hw.yaroslav_belaychuk.lesson006HW import zadacha_7


def test_function() -> None:
    y1 = User02(date(2020, 1, 23))
    b2 = User02(123)
    d1 = date(year=1987, month=8, day=2)
    d2 = (1987, 8, 2)
    f1 = {"nik": date(1988, 8, 2), "vika": date(1953, 5, 9)}
    d6 = "[1, 1, 1, 1, 2, 2, 3]"
    d3 = 123
    d4 = [1, 1, 1, 1, 2, 2, 3]
    d5 = {1, 2, 3, 4}
    c5 = DupCounter05(d6)
    c1 = DupCounter05(d3)
    c3 = DupCounter05(d4)
    c4 = DupCounter05(d5)
    obj = Multiplier04()
    obj.add(4).add("x")
    assert palindrom("") == {"data": True}
    assert palindrom("x") == {"data": True}
    assert palindrom("xx") == {"data": True}
    assert palindrom("xy") == {"data": False}
    assert palindrom("xx x") == {"data": False}
    assert palindrom("xX") == {"data": False}
    assert palindrom("xy") == {"data": False}
    assert "errors" in palindrom(1)
    assert umnogenie(1, 2, 3) == {"data": 6}
    assert umnogenie(1) == {"data": 1}
    assert umnogenie(1, 2) == {"data": 2}
    assert umnogenie("1", 3) == {"data": "111"}
    assert umnogenie(2, "a") == {"data": "aa"}
    assert umnogenie(2, [2]) == {"data": [2, 2]}
    assert umnogenie(2, [2], 2) == {"data": [2, 2, 2, 2]}
    assert "errors" in umnogenie(2, [2], 2, [2])
    assert date_age(d1) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert "errors" in date_age(d2)
    assert "errors" in date_age(...)
    assert zadacha_4(f1) == {"data": "vika"}
    assert "errors" in zadacha_4({})
    assert "errors" in zadacha_4({1: 1j, 2: 2j})
    assert "errors" in zadacha_4(1)
    assert zadacha_5(("a", "a", 1, 2)) == {"data": {"a": 2}}
    assert zadacha_5([(), "", "", 1]) == {"data": {"": 2}}
    assert zadacha_5({}) == {"data": {}}
    assert zadacha_5([]) == {"data": {}}
    assert "errors" in zadacha_5([[], []])
    assert zadacha_5("abc") == {"data": {}}
    assert zadacha_5("aaa") == {"data": {"a": 3}}
    assert "errors" in zadacha_5([{}, {}, set()])
    assert zadacha_7("a3b4c2") == {"data": "aaabbbbcc"}
    assert "errors" in zadacha_7("a3b2c")
    assert "errors" in zadacha_7(["a3b4c5"])
    assert zadacha_7("a11") == {"data": "aaaaaaaaaaa"}
    assert zadacha_7("a0") == {"data": ""}
    assert zadacha_7("a1") == {"data": "a"}
    assert zadacha_7("a2b2a1") == {"data": "aabba"}
    assert "errors" in zadacha_7("a")
    assert zadacha_7("") == {"data": ""}
    assert (c5.get_dups()) == {"1": 4, ",": 6, " ": 6, "2": 2}
    assert (c3.get_dups()) == {1: 4, 2: 2}
    assert (c4.get_dups()) == {}
    assert "errors" in c1.get_dups()
    assert y1.age == 2
    assert "errors" in b2.age
    assert obj.get_result() == "xxxx"
    assert Palindrome01("xyx")
    assert not Palindrome01("xy x")
