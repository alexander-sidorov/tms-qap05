from hw.maria_saganovich.lesson6_hw.lvl12_even_keys_odd_values import (
    func12_even_keys_odd_values,
)


def test_func12_even_keys_odd_values() -> None:
    assert func12_even_keys_odd_values(1, 2) == {"data": {1: 2}}
    assert func12_even_keys_odd_values(1, 2, 3, 4) == {"data": {1: 2, 3: 4}}
    assert func12_even_keys_odd_values(1, 2, 3, 4, 5, 7, 6, 9) == {
        "data": {1: 2, 3: 4, 5: 7, 6: 9}
    }
    assert func12_even_keys_odd_values(1, 2, 3, 4, 5, 6, 8, 10) == {
        "data": {1: 2, 3: 4, 5: 6, 8: 10}
    }
    assert func12_even_keys_odd_values(1, "", 3, 4) == {
        "errors": ["should be number"]
    }
    assert func12_even_keys_odd_values(1, "", 3, "") == {
        "errors": ["should be number", "should be number"]
    }
