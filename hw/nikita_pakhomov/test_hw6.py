from datetime import date

from hw.nikita_pakhomov.nlesson3.hw6 import is_palindrome
from hw.nikita_pakhomov.nlesson3.hw6 import level_2
from hw.nikita_pakhomov.nlesson3.hw6 import level_3
from hw.nikita_pakhomov.nlesson3.hw6 import level_4


def test_is_palindrome() -> None:
    assert is_palindrome("") == {"data": True}
    assert is_palindrome("x") == {"data": True}
    assert is_palindrome("xx") == {"data": True}
    assert is_palindrome("xy") == {"data": False}


def test_level_2() -> None:
    assert level_2(1) == {"data": 1}
    assert level_2(1, 2) == {"data": 2}
    assert level_2(1, 2, 3) == {"data": 6}


def test_level_3() -> None:
    date_variable = date(year=1987, month=8, day=2)
    assert level_3(date_variable) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }


def test_level_4() -> None:
    datys = {
        "A": date(year=2021, month=3, day=1),
        "B": date(year=1999, month=4, day=1),
    }
    datys_1 = {
        "A": date(year=1999, month=4, day=1),
        "B": date(year=2021, month=3, day=1),
    }

    assert level_4(datys) == {"data": "B"}
    assert level_4([]) == {"errors": "this is not a date"}
    assert level_4(datys_1) == {"data": "A"}
