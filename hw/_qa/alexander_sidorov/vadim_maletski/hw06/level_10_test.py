from typing import Any

import pytest

from hw.vadim_maletski.func6 import level_10

from .common import azaza
from .common import validate_data
from .common import validate_errors

happy_data = [  # noqa: ECE001
    pytest.param(arg1, arg2, expected, id=name)
    for name, (arg1, arg2, expected) in {
        "v-01": ("", "", {}),
        "v-02": ("", "a", {...: ["a"]}),
        "v-03": ("a", "", {"a": None}),
        "v-04": ("a", azaza("1", bs=[list]), {"a": "1"}),
        "v-05": ("a", azaza("2", bs=[str]), {"a": "2"}),
        "v-06": ("a", azaza([3], bs=[tuple]), {"a": 3}),
        "v-07": ("a", azaza(bs=[list]), {"a": None}),
        "v-08": ("a", azaza(bs=[str]), {"a": None}),
        "v-09": ("a", azaza(bs=[tuple]), {"a": None}),
        "v-11": ("aa", "1", {"a": None}),
        "v-12": ("aa", "12", {"a": "2"}),
        "v-13": ("ab", "12", {"a": "1", "b": "2"}),
        "v-14-1": ("ab", [1, 2], {"a": 1, "b": 2}),
        "v-14-2": ([1, 2], "ab", {1: "a", 2: "b"}),
        "v-15": (azaza("1", bs=[list]), "a", {"1": "a"}),
        "v-16": (azaza("2", bs=[str]), "a", {"2": "a"}),
        "v-17": (azaza("3", bs=[tuple]), "a", {3: "a"}),
        "v-18": (azaza(bs=[list]), "a", {...: ["a"]}),
        "v-19": (azaza(bs=[str]), "a", {...: ["a"]}),
        "v-20": (azaza(bs=[tuple]), "a", {...: ["a"]}),
    }.items()
]


@pytest.mark.parametrize("arg1,arg2,expected", happy_data)
def test_task_10_happy(arg1: Any, arg2: Any, expected: Any) -> None:
    outcome = level_10(arg1, arg2)
    validate_data(outcome)

    data = outcome["data"]
    assert data == expected


unhappy_data = [
    pytest.param(arg1, arg2, id=name)
    for name, (arg1, arg2) in {
        "invalid-type-dict-dict": ({}, {}),
        "invalid-type-dict-set": ({}, set()),
        "invalid-type-list-x": (azaza(bs=[list]), azaza()),
        "invalid-type-range-x": (range(10), azaza()),
        "invalid-type-set-dict": (set(), {}),
        "invalid-type-set-set": (set(), set()),
        "invalid-type-str-x": (azaza(bs=[str]), azaza()),
        "invalid-type-tuple-x": (azaza(bs=[tuple]), azaza()),
        "invalid-type-x-list": (azaza(), azaza(bs=[list])),
        "invalid-type-x-range": (azaza(), range(10)),
        "invalid-type-x-str": (azaza(), azaza(bs=[str])),
        "invalid-type-x-tuple": (azaza(), azaza(bs=[tuple])),
        "invalid-type-x-x": (azaza(), azaza()),
        "invalid-type-xdict-xdict": (azaza(bs=[dict]), azaza(bs=[dict])),
        "invalid-type-xdict-xset": (azaza(bs=[dict]), azaza(bs=[set])),
        "invalid-type-xset-xdict": (azaza(bs=[set]), azaza(bs=[dict])),
        "invalid-type-xset-xset": (azaza(bs=[set]), azaza(bs=[set])),
    }.items()
]


@pytest.mark.parametrize("arg1,arg2", unhappy_data)
def test_task_10_unhappy(arg1: Any, arg2: Any) -> None:
    outcome = level_10(arg1, arg2)
    validate_errors(outcome)
