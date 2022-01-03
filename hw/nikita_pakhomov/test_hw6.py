from hw.nikita_pakhomov.nlesson3.hw6 import is_palindrome


def test_is_palindrome() -> None:
    assert is_palindrome("") == {"data": True}
    assert is_palindrome("x") == {"data": True}
    assert is_palindrome("xx") == {"data": True}
    assert is_palindrome("xy") == {"data": False}
