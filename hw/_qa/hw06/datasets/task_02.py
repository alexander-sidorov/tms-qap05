import pytest

from hw._qa.hw06.common import azaza

happy_data = [  # type: ignore  # noqa: ECE001
    pytest.param(args, expected, id=name)  # type: ignore
    for name, (args, expected) in {
        "b-b": [(True, False), 0],
        "c-c": [(1j, 1j), -1],
        "f-i": [(0.25, 2, 2), 1],
        "fl-c": [(2.0, 3j), 6.0j],
        "i-c": [(2, 3j), 6j],
        "i-f": [(2, 3.0), 6.0],
        "i-i-i": [(1, 2, 3), 6],
        "i-i": [(2, 3), 6],
        "i-l-i": [(2, [1], 2), [1, 1, 1, 1]],
        "i-s-i": [(2, "a", 2), "aaaa"],
        "i-s": [(2, "a"), "aa"],
        "i-t-i": [(2, (1,), 2), (1, 1, 1, 1)],
        "s-i": [("a", 2), "aa"],
        "s": [("",), ""],
        "t-i": [((3,), 2), (3, 3)],
        "xl-i": [(azaza([1], bs=[list]), 2), [1, 1]],
        "xs-i": [(azaza("ab", bs=[str]), 2), "abab"],
        "z-z": [(0, 0), 0],
    }.items()
]

unhappy_data = [
    pytest.param(args, id=name)
    for name, args in {
        "mul-d-i": [{}, 1],
        "mul-n-i": [None, 1],
        "mul-s-c": ["a", 2j],
        "mul-s-f": ["a", 2.0],
        "mul-s-l": ["a", azaza(bs=[list])],
        "mul-x": [azaza(), azaza()],
        "no-data": [],
        "type": [azaza()],
    }.items()
]
