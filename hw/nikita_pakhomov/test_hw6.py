from hw.nikita_pakhomov.nlesson3.hw6 import is_palindrome
from hw.nikita_pakhomov.nlesson3.hw6 import level_2


def test_is_palindrome() -> None:
    assert is_palindrome("") == {"data": True}
    assert is_palindrome("x") == {"data": True}
    assert is_palindrome("xx") == {"data": True}
    assert is_palindrome("xy") == {"data": False}


def test_level_2() -> None:
    assert level_2(1) == {"data": 1}
    assert level_2(1, 2) == {"data": 2}
    assert level_2(1, 2, 3) == {"data": 6}
