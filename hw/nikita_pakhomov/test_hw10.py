from datetime import date

from hw.nikita_pakhomov.nlesson3.hw10 import Palindrome01
from hw.nikita_pakhomov.nlesson3.hw10 import User02


def test_is_palindrome01() -> None:
    assert Palindrome01("xyx")
    assert not Palindrome01("xy x")


def test_is_user02() -> None:
    ddd = date(2020, 1, 23)
    assert User02(ddd).age() == 2
