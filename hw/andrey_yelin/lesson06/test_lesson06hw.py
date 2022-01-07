from datetime import date

from hw.andrey_yelin.lesson06.functions_lesson06hw import ageResult
from hw.andrey_yelin.lesson06.functions_lesson06hw import isPalindrome
from hw.andrey_yelin.lesson06.functions_lesson06hw import multiplyArgs
from hw.andrey_yelin.lesson06.functions_lesson06hw import older
from hw.andrey_yelin.lesson06.functions_lesson06hw import repeatingElements


def test_isPalindrome() -> None:  # noqa: N802
    assert isPalindrome("") == {"data": True}
    assert isPalindrome("x") == {"data": True}
    assert isPalindrome("xx") == {"data": True}
    assert isPalindrome("xy") == {"data": False}
    assert isPalindrome(None) == {"errors": "none argument"}
    assert isPalindrome(1) == {"errors": "not a string"}


def test_multiplyArgs() -> None:  # noqa: N802
    assert multiplyArgs(1) == {"data": 1}
    assert multiplyArgs(1, 2) == {"data": 2}
    assert multiplyArgs(1, 2, 3) == {"data": 6}
    assert multiplyArgs() == {"errors": "empty arguments"}
    assert multiplyArgs(1, "a") == {"errors": "variable is not a number"}


def test_ageResult() -> None:  # noqa: N802
    d = date(year=1987, month=8, day=2)  # noqa: VNE001
    assert ageResult(d) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert ageResult(2) == {"errors": "variable is not a date"}


def test_older() -> None:
    b = {  # noqa: VNE001
        "A": date(year=2021, month=7, day=18),
        "B": date(year=1993, month=6, day=27),
    }
    assert older(b) == {"data": "B"}
    assert older([]) == {"errors": "empty variable"}
    assert older({}) == {"errors": "empty variable"}


def test_repeatingElements() -> None:  # noqa: N802
    c = [(), "", "", 1]  # noqa: VNE001
    assert repeatingElements(c) == {"data": {"": 2}}
