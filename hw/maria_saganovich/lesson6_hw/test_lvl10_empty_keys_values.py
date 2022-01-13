from hw.maria_saganovich.lesson6_hw.lvl10_empty_keys_values import (
    func10_empty_keys_values,
)


def test_func10_empty_keys_values() -> None:
    assert func10_empty_keys_values("abc", [1, 2]) == {
        "data": {"a": 1, "b": 2, "c": None}
    }
    assert func10_empty_keys_values("ab", [1, 2, 3]) == {
        "data": {"a": 1, "b": 2, ...: [3]}
    }
    assert func10_empty_keys_values("ab", [1, 2, 3, 4]) == {
        "data": {"a": 1, "b": 2, ...: [3, 4]}
    }
    assert func10_empty_keys_values("", [1, 2, 3]) == {
        "data": {...: [1, 2, 3]}
    }
    assert func10_empty_keys_values("sdv", []) == {
        "data": {"s": None, "d": None, "v": None}
    }
    assert func10_empty_keys_values("sdv", {}) == {  # noqa: JS101
        "errors": ["Invalid arguments"]
    }
    assert func10_empty_keys_values("", []) == {"data": {}}
    assert func10_empty_keys_values([], []) == {"data": {}}
