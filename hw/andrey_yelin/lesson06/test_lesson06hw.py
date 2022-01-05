from datetime import date

from hw.andrey_yelin.lesson06.functions_lesson06hw import ageResult
from hw.andrey_yelin.lesson06.functions_lesson06hw import isPalindrome
from hw.andrey_yelin.lesson06.functions_lesson06hw import multiplyArgs


def test_isPalindrome() -> None:
    assert isPalindrome("") == {"data": True}
    assert isPalindrome("x") == {"data": True}
    assert isPalindrome("xx") == {"data": True}
    assert isPalindrome("xy") == {"data": False}


def test_multiplyArgs() -> None:
    assert multiplyArgs(1) == {"data": 1}
    assert multiplyArgs(1, 2) == {"data": 2}
    assert multiplyArgs(1, 2, 3) == {"data": 6}


def test_ageResult() -> None:
    d = date(year=1987, month=8, day=2)
    assert ageResult(d) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
