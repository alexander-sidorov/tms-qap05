from datetime import date

from hw.andrei_bondar.lesson_06hw import argum1
from hw.andrei_bondar.lesson_06hw import datrog
from hw.andrei_bondar.lesson_06hw import palindrome


def test_palindrom() -> None:
    assert palindrome("") == {"data": True}
    assert palindrome(" ") == {"data": True}
    assert palindrome("x") == {"data": True}
    assert palindrome("xy") == {"data": False}
    assert palindrome("xx") == {"data": True}


def test_argum1() -> None:
    assert argum1(1) == {"data": 1}
    assert argum1(1, 2) == {"data": 2}
    assert argum1(1, 2, 3) == {"data": 6}


def test_datrog() -> None:
    d1 = date(year=1987, month=8, day=2)
    d2 = date(year=1911, month=1, day=1)

    assert datrog(d1) == {
        "date": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert datrog(d2) == {
        "date": {"year": 1911, "month": 1, "day": 1, "age": 111}
    }
