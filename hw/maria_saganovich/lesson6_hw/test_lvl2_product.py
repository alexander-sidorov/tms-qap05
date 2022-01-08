from hw.maria_saganovich.lesson6_hw.lvl2_product import func2_product


def test_func2_product() -> None:
    assert func2_product(1) == {"data": 1}
    assert func2_product(1, 2) == {"data": 2}
    assert func2_product(1, 2, 3) == {"data": 6}
    assert func2_product("abc", 3, 4) == {"errors": ["should be number(s)"]}
    assert func2_product(5, 3, "abc") == {"errors": ["should be number(s)"]}
    assert func2_product("abc", "def") == {"errors": ["should be number(s)"]}
    assert func2_product(2, -21.9) == {"data": -43.8}
    assert func2_product(2, 0, 1) == {"data": 0}
    assert func2_product((1+2j), (3+4j)) == {"data": (-5 + 10j)}
