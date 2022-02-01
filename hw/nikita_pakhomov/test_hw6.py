from datetime import date

from hw.nikita_pakhomov.nlesson3.hw6 import is_palindrome
from hw.nikita_pakhomov.nlesson3.hw6 import level_2
from hw.nikita_pakhomov.nlesson3.hw6 import level_3
from hw.nikita_pakhomov.nlesson3.hw6 import level_4_1
from hw.nikita_pakhomov.nlesson3.hw6 import level_5
from hw.nikita_pakhomov.nlesson3.hw6 import level_7
from hw.nikita_pakhomov.nlesson3.hw6 import level_8


def test_is_palindrome() -> None:
    assert is_palindrome("") == {"data": True}
    assert is_palindrome("x") == {"data": True}
    assert is_palindrome("xx") == {"data": True}
    assert is_palindrome("xy") == {"data": False}
    assert is_palindrome("xX") == {"data": False}
    assert is_palindrome(123) == {'errors': 'invalid input'}


def test_level_2() -> None:
    assert level_2(1) == {"data": 1}
    assert level_2(1, 2) == {"data": 2}
    assert level_2(1, 2, 3) == {"data": 6}
    assert level_2(1, 2, 'j') == {'errors': 'invalid input'}


def test_level_3() -> None:
    date_variable = date(year=1987, month=8, day=2)
    assert level_3(date_variable) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }


def test_level_4_1() -> None:
    datys = {
        "A": date(year=2021, month=3, day=1),
        "B": date(year=1999, month=4, day=1),
    }
    datys_1 = {
        "A": date(year=1999, month=4, day=1),
        "B": date(year=2021, month=3, day=1),
    }
    datys_2 = {
        "A": date(year=1999, month=4, day=1),
        "B": date(year=1999, month=4, day=1),
    }

    assert level_4_1(datys) == {"data": "B"}
    assert level_4_1(datys_1) == {"data": "A"}
    assert level_4_1(datys_2) == {"data": "A"}


def test_level_5() -> None:
    elements = [(), "", "", 1]
    assert level_5(elements) == {"data": {"": 2}}
    assert level_5([]) == {"data": {}}


def test_level_7() -> None:
    assert level_7("a1b1a1") == {"data": "aba"}
    assert level_7("a3bc") == {'errors': 'invalid input'}
    assert level_7("13b2c1") == {'errors': 'invalid input'}
    assert level_7("a3b2cv") == {'errors': 'invalid input'}
    assert level_7("b5") == {"data": "bbbbb"}


def test_level_8() -> None:
    assert level_8("aaabb") == {"data": "a3b2"}
    assert level_8("aaabb111!!") == {"data": "a3b213!2"}
    assert level_8(12345) == {'errors': 'invalid input'}
    assert level_8("") == {"data": ""}
    assert level_8("a") == {"data": "a1"}
