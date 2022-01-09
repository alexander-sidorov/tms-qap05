from hw.maria_saganovich.lesson6_hw.lvl5_duplicate_elements import (
    func5_duplicate_elements,
)


def test_func5_duplicate_elements() -> None:
    c = [(), "", "", 1]
    c1 = [10, 10, 23, 10, 123, 66, 78, 123]
    c2 = ()
    c3 = []
    c4 = ["may", "day"]
    assert func5_duplicate_elements(c) == {"data": {"": 2}}
    assert func5_duplicate_elements(c1) == {"data": {10: 3, 123: 2}}
    assert func5_duplicate_elements(c2) == {"errors": ["arg should be list"]}
    assert func5_duplicate_elements(c3) == {
        "errors": ["list shouldn't be empty"]
    }
    assert func5_duplicate_elements(c4) == {"data": ["no duplicates"]}
