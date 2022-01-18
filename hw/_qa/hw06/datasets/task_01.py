import pytest

from hw._qa.hw06.common import azaza

happy_data = [
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "empty": ["", True],
        "v-Aa_a": ["Aa a", False],
        "v-aa-x": [azaza("aa", bs=[str]), True],
        "v-Aa": ["Aa", False],
        "v-aa": ["aa", True],
        "v-aaa": ["aaa", True],
        "v-ab-x": [azaza("ab", bs=[str]), False],
        "v-ab": ["ab", False],
        "v-aba": ["aba", True],
    }.items()
]


unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "type": azaza(),
    }.items()
]
