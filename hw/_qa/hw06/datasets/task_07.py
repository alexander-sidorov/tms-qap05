import pytest

from hw._qa.hw06.common import azaza

happy_data = [
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "empty-x": (azaza("", bs=[str]), ""),
        "empty": ("", ""),
        "v-a0": ("a0", ""),
        "v-a1-x": (azaza("a1", bs=[str]), "a"),
        "v-a1": ("a1", "a"),
        "v-a11": ("a11", "aaaaaaaaaaa"),
        "v-a1b11a1": ("a1b11a1", "abbbbbbbbbbba"),
        "v-a1b2": ("a1b2", "abb"),
        "v-a1b2a1": ("a1b2a1", "abba"),
        "v-a3": ("a3", "aaa"),
    }.items()
]

unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "v-1": "1",
        "v-1a": "1a",
        "v-1a1": "1a1",
        "v-a": "a",
        # "v-aa1": "aa1",  # valid issue
        "type": azaza(),
    }.items()
]
