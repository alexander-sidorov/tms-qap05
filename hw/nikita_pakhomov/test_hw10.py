from hw.nikita_pakhomov.nlesson3.hw10 import Palindrome01


def test_is_palindrome01() -> None:
    assert Palindrome01("xyx")
    assert not Palindrome01("xy x")
