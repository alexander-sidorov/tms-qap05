from hw.siarhei_apanel.refakt import palindrom


def test_func1_palindrome() -> None:
    args = palindrom("Do geese see God")
    assert palindrom(args) == {"data": True}
