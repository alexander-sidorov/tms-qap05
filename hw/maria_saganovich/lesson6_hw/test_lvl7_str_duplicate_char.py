from hw.maria_saganovich.lesson6_hw.lvl7_str_duplicate_char import (
    func7_str_duplicate_char,
)


def test_func7_str_duplicate_char() -> None:
    assert func7_str_duplicate_char("a3b2c1") == {"data": "aaabbc"}
    assert func7_str_duplicate_char("aaa3b2c1") == {"data": "aaaaaaaaabbc"}
    assert func7_str_duplicate_char("") == {"errors": ["str is empty"]}
    assert func7_str_duplicate_char([]) == {"errors": ["arg should be str"]}
