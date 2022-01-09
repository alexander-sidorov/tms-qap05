from hw.maria_saganovich.lesson6_hw.lvl8_duplicate_char_number import func8_duplicate_char_number


def test_func8_duplicate_char_number() -> None:
    assert func8_duplicate_char_number("aaabb") == {"data": "a3b2"}
    assert func8_duplicate_char_number("aaa777bb") == {"data": "a373b2"}
    assert func8_duplicate_char_number("") == {"errors": ["str is empty"]}
    assert func8_duplicate_char_number([]) == {"errors": ["arg should be str"]}
