from hw.maria_saganovich.lesson6_hw.lvl2_product import func2_product


def test_func2_product() -> None:
    assert func2_product(1) == {"data": 1}
    assert func2_product(1, 2) == {"data": 2}
    assert func2_product(1, 2, 3) == {"data": 6}
    assert func2_product("abc", 3, 4) == {
        "data": "abcabcabcabcabcabcabcabcabcabcabcabc"
    }
    assert func2_product(5, 3, "abc") == {
        "data": "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    }
    assert func2_product("abc", "def") == {
        "errors": ["Can't multiply sequence by non-int of types"]
    }
    assert func2_product(2, -21.9) == {"data": -43.8}
    assert func2_product(2, 0, 1) == {"data": 0}
    assert func2_product((1 + 2j), (3 + 4j)) == {"data": (-5 + 10j)}
    assert func2_product(2, "a") == {"data": "aa"}
    assert func2_product(2, [2]) == {"data": [2, 2]}
    assert func2_product(2, [2], 2) == {"data": [2, 2, 2, 2]}
    assert func2_product(2, [2], 2, [2]) == {
        "errors": ["Can't multiply sequence by non-int of types"]
    }
