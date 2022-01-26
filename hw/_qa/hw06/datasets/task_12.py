# pylint: disable=redefined-builtin


from functools import partial

import pytest

from hw._qa.hw06.common import azaza

complex = partial(azaza, bs=[complex])  # noqa: A001,VNE003
float = partial(azaza, bs=[float])  # noqa: A001,VNE003
int = partial(azaza, bs=[int])  # noqa: A001,VNE003
list = partial(azaza, bs=[list])  # noqa: A001,VNE003
set = partial(azaza, bs=[set])  # noqa: A001,VNE003
dict = partial(azaza, bs=[dict])  # noqa: A001,VNE003
str = partial(azaza, bs=[str])  # noqa: A001,VNE003
tuple = partial(azaza, bs=[tuple])  # noqa: A001,VNE003

happy_data = [  # type: ignore  # noqa: ECE001
    pytest.param(args, expected, id=name)
    for name, (args, expected) in {
        "empty": [
            (),
            {},
        ],
        "v-1": [
            (
                complex(1j),
                int(1),
            ),
            {
                1j: 1,
            },
        ],
        "v-2": [
            (
                str(),
                str(),
                ...,
                None,
                None,
                ...,
            ),
            {
                "": "",
                ...: None,
                None: ...,
            },
        ],
        "v-3": [
            (
                str(),
                list(),  # noqa: C408
                tuple(),  # noqa: C408
                set(),
                print,  # noqa: T002
                dict(),  # noqa: C408
            ),
            {
                "": [],
                (): set(),
                print: {},  # noqa: T002
            },
        ],
    }.items()
]

unhappy_data = [
    pytest.param(args, id=name)
    for name, args in {
        "odd-1": [1],
        "odd-3": [1, 2, 3],
        "hash-1": [[], "a"],
        "hash-2": ["a", "b", list(), "c"],  # noqa: C408
        "hash-3": ["a", "b", dict(), "c"],  # noqa: C408
        "hash-4": ["a", "b", set(), "c"],
    }.items()
]
