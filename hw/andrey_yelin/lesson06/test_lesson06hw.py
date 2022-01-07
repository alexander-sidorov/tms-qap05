from datetime import date

from hw.andrey_yelin.lesson06.functions_lesson06hw import ageResult
from hw.andrey_yelin.lesson06.functions_lesson06hw import isPalindrome
from hw.andrey_yelin.lesson06.functions_lesson06hw import multiplyArgs
from hw.andrey_yelin.lesson06.functions_lesson06hw import older
from hw.andrey_yelin.lesson06.functions_lesson06hw import repeatingElements


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


def test_older() -> None:
    b = {
        "A": date(year=2021, month=7, day=18),
        "B": date(year=1993, month=6, day=27),
    }
    assert older(b) == {"data": "B"}


def test_repeatingElements() -> None:
    c = [(), "", "", 1]
    assert repeatingElements(c) == {"data": {"": 2}}
