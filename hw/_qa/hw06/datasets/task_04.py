from datetime import date

import pytest

from hw._qa.hw06.common import azaza

happy_data = [
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "date": [{object: date(1900, 1, 1), type: date(1800, 1, 1)}, type],
        "xdate": [
            {
                object: azaza(1900, 1, 1, bs=[date]),
                type: azaza(1800, 1, 1, bs=[date]),
            },
            type,
        ],
    }.items()
]


unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "cmp": {2: azaza(), 1: azaza()},
        "empty": {},
        "type": azaza(),
    }.items()
]
