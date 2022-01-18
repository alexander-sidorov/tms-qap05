import pytest

from hw._qa.hw06.common import azaza

happy_data = [
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "dict-0-x": (azaza(bs=[dict]), {}),
        "dict-0": ({}, {}),
        "dict-1-x": (azaza({1: 100}, bs=[dict]), {}),
        "dict-1": ({1: 100}, {}),
        "frozenset-0-x": (azaza(bs=[frozenset]), {}),
        "frozenset-0": (frozenset(), {}),
        "frozenset-1-x": (azaza({1}, bs=[frozenset]), {}),
        "frozenset-1": (frozenset({1}), {}),
        "list-0-x": (azaza(bs=[list]), {}),
        "list-0": ([], {}),
        "list-1-x": (azaza([1], bs=[list]), {}),
        "list-1": ([1], {}),
        "list-2-x": (azaza([1, 1], bs=[list]), {1: 2}),
        "list-2": ([1, 1], {1: 2}),
        "range": (range(10), {}),
        "set-0-x": (azaza(bs=[set]), {}),
        "set-0": (set(), {}),
        "set-1-x": (azaza({1}, bs=[set]), {}),
        "set-1": ({1}, {}),
        "str-0-x": (azaza("", bs=[str]), {}),
        "str-0": ("", {}),
        "str-1-x": (azaza("a", bs=[str]), {}),
        "str-1": ("a", {}),
        "str-2-x": (azaza("aa", bs=[str]), {"a": 2}),
        "str-2": ("aa", {"a": 2}),
        "tuple-0-x": (azaza((), bs=[tuple]), {}),
        "tuple-0": ((), {}),
        "tuple-1-x": (azaza((1,), bs=[tuple]), {}),
        "tuple-1": ((1,), {}),
        "tuple-2-x": (azaza((1, 1), bs=[tuple]), {1: 2}),
        "tuple-2": ((1, 1), {1: 2}),
    }.items()
]


aza = azaza(bs=[dict])
azz = azaza(bs=[set])

unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "hash": [aza, aza, azz, azz],
        "type": azaza(),
    }.items()
]
