from hw.maria_saganovich.lesson6_hw.lvl8_duplicate_char_number import (
    func8_duplicate_char_number,
)


def test_func8_duplicate_char_number() -> None:
    assert func8_duplicate_char_number("aaabb") == {"data": "a3b2"}
    assert func8_duplicate_char_number("aaa777bb") == {
        "errors": ["Unsupported type 'int'"]
    }
    assert func8_duplicate_char_number("") == {"data": ""}
    assert func8_duplicate_char_number([]) == {"errors": ["Invalid argument"]}
    assert func8_duplicate_char_number("aba") == {"data": "a1b1a1"}
