import pytest

from hw._qa.hw06.common import azaza

happy_data = [  # noqa: ECE001
    pytest.param(arg1, arg2, expected, id=name)
    for name, (arg1, arg2, expected) in {
        "l-empty-empty-x": (azaza(bs=[list]), azaza(bs=[list]), {}),
        "l-empty-empty": ([], [], {}),
        "s-empty-empty-x": (azaza(bs=[str]), "", {}),
        "s-empty-empty": ("", "", {}),
        "t-empty-empty-x": ((), azaza(bs=[tuple]), {}),
        "t-empty-empty": ((), (), {}),
        "v-01": ("", "a", {...: ["a"]}),
        "v-02": ("a", "", {"a": None}),
        "v-03": ("a", azaza("1", bs=[list]), {"a": "1"}),
        "v-04": ("a", azaza("2", bs=[str]), {"a": "2"}),
        "v-05": ("a", azaza([3], bs=[tuple]), {"a": 3}),
        "v-06": ("a", azaza(bs=[list]), {"a": None}),
        "v-07": ("a", azaza(bs=[str]), {"a": None}),
        "v-08": ("a", azaza(bs=[tuple]), {"a": None}),
        "v-09": ("aa", "1", {"a": None}),
        "v-10": ("aa", "12", {"a": "2"}),
        "v-11": ("ab", "12", {"a": "1", "b": "2"}),
        "v-12": ("ab", [1, 2], {"a": 1, "b": 2}),
        "v-13": ([1, 2], "ab", {1: "a", 2: "b"}),
        "v-14": (azaza("1", bs=[list]), "a", {"1": "a"}),
        "v-15": (azaza("2", bs=[str]), "a", {"2": "a"}),
        "v-16": (azaza("3", bs=[tuple]), "a", {"3": "a"}),
        "v-17": (azaza(bs=[list]), "a", {...: ["a"]}),
        "v-18": (azaza(bs=[str]), "a", {...: ["a"]}),
        "v-19": (azaza(bs=[tuple]), "a", {...: ["a"]}),
    }.items()
]


unhappy_data = [
    pytest.param(arg1, arg2, id=name)
    for name, (arg1, arg2) in {
        "dict-dict": ({}, {}),
        "dict-set": ({}, set()),
        "list-x": (azaza(bs=[list]), azaza()),
        "range-x": (range(10), azaza()),
        "set-dict": (set(), {}),
        "set-set": (set(), set()),
        "str-x": (azaza(bs=[str]), azaza()),
        "tuple-x": (azaza(bs=[tuple]), azaza()),
        "x-list": (azaza(), azaza(bs=[list])),
        "x-range": (azaza(), range(10)),
        "x-str": (azaza(), azaza(bs=[str])),
        "x-tuple": (azaza(), azaza(bs=[tuple])),
        "x-x": (azaza(), azaza()),
        "xdict-xdict": (azaza(bs=[dict]), azaza(bs=[dict])),
        "xdict-xset": (azaza(bs=[dict]), azaza(bs=[set])),
        "xset-xdict": (azaza(bs=[set]), azaza(bs=[dict])),
        "xset-xset": (azaza(bs=[set]), azaza(bs=[set])),
    }.items()
]
