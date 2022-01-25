import pytest

from hw._qa.hw06.common import azaza

happy_data = [
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "empty": ("", ""),
        "v-a-x": (azaza("a", bs=[str]), "a1"),
        "v-a": ("a", "a1"),
        "v-aaa": ("aaa", "a3"),
        "v-aaaaaaaaaaa": ("aaaaaaaaaaa", "a11"),
        "v-abba": ("abba", "a1b2a1"),
        "v-abbbbbbbbbbba": ("abbbbbbbbbbba", "a1b11a1"),
    }.items()
]

unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "type": azaza(),
        "v-1-x": azaza("1", bs=[str]),
        "v-1": "1",
        "v-1a": "1a",
        "v-1a1": "1a1",
        "v-a1": "a1",
        "v-aa1": "aa1",
    }.items()
]
