from hw.maria_saganovich.lesson6_hw.lvl1_palindrome import func1_palindrome


def test_func1_palindrome() -> None:
    assert func1_palindrome("") == {"data": True}
    assert func1_palindrome("x") == {"data": True}
    assert func1_palindrome("xx") == {"data": True}
    assert func1_palindrome("xy") == {"data": False}
    assert func1_palindrome(["x", "y"]) == {"data": False}
    assert func1_palindrome("Xx") == {"data": False}
    assert func1_palindrome("Do geese see God") == {"data": False}
    assert func1_palindrome("Do geese    se e God  ") == {"data": False}
