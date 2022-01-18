import pytest

from hw._qa.hw06.common import azaza

zzz = azaza()

happy_data = [  # noqa: ECE001
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "empty-x": (azaza(bs=[dict]), {}),
        "empty": ({}, {}),
        "v-01": ({1: 100, 2: 100, 3: 300}, {100: [1, 2], 300: 3}),
        "v-02": ({1: (), 2: None, 3: ...}, {...: 3, None: 2, (): 1}),
        "v-03": ({1: zzz}, {zzz: 1}),
    }.items()
]


unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "hash": {1: []},
        "type": azaza(),
    }.items()
]
