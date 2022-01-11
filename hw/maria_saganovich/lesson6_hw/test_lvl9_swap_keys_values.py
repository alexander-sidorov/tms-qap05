from hw.maria_saganovich.lesson6_hw.lvl9_swap_keys_values import (
    func9_swap_keys_values,
)


def test_func9_swap_keys_values() -> None:
    assert func9_swap_keys_values({1: 100, 2: 100, 3: 300}) == {  # noqa: JS101
        "data": {100: [1, 2], 300: [3]}
    }
    assert func9_swap_keys_values({1: 100, 2: 200, 3: 300}) == {  # noqa: JS101
        "data": {100: [1], 200: [2], 300: [3]}
    }
    assert func9_swap_keys_values("{1: 100, 2: 100, 3: 300}") == {
        "errors": ["Unsupported type"]
    }
    assert func9_swap_keys_values({}) == {"data": {}}
