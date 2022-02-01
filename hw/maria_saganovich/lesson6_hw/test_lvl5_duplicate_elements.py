from hw.maria_saganovich.lesson6_hw.lvl5_duplicate_elements import (
    func5_duplicate_elements,
)


def test_func5_duplicate_elements() -> None:
    c0 = [(), "", "", 1]
    c1 = [10, 10, 23, 10, 123, 66, 78, 123]
    c2 = ()
    c3: list = []
    c4 = ["may", "day"]
    assert func5_duplicate_elements(c0) == {"data": {"": 2}}
    assert func5_duplicate_elements(c1) == {"data": {10: 3, 123: 2}}
    assert func5_duplicate_elements(c2) == {"data": {}}
    assert func5_duplicate_elements(c3) == {"data": {}}
    assert func5_duplicate_elements(c4) == {"data": {}}
    assert func5_duplicate_elements((1, 2, 3)) == {"data": {}}
    assert func5_duplicate_elements((1, 1, 1)) == {"data": {1: 3}}
    assert func5_duplicate_elements("aaa") == {"data": {"a": 3}}
    assert func5_duplicate_elements([[], []]) == {
        "errors": ["Unhashable type: 'list'"]
    }
