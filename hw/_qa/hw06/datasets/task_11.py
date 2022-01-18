import pytest

from hw._qa.hw06.common import azaza

happy_data = [  # noqa: ECE001
    pytest.param(arg1, arg2, id=name)
    for name, (arg1, arg2) in {
        "v-e-ff-ff": (frozenset(), frozenset()),
        "v-e-ff-fx": (frozenset(), azaza(bs=[frozenset])),
        "v-e-ff-ss": (frozenset(), set()),
        "v-e-ff-sx": (frozenset(), azaza(bs=[set])),
        "v-e-fx-ff": (azaza(bs=[frozenset]), frozenset()),
        "v-e-fx-fx": (azaza(bs=[frozenset]), azaza(bs=[frozenset])),
        "v-e-fx-ss": (azaza(bs=[frozenset]), set()),
        "v-e-fx-sx": (azaza(bs=[frozenset]), azaza(bs=[set])),
        "v-e-ss-ff": (set(), frozenset()),
        "v-e-ss-fx": (set(), azaza(bs=[frozenset])),
        "v-e-ss-ss": (set(), set()),
        "v-e-ss-sx": (set(), azaza(bs=[set])),
        "v-e-sx-ff": (azaza(bs=[set]), frozenset()),
        "v-e-sx-fx": (azaza(bs=[set]), azaza(bs=[frozenset])),
        "v-e-sx-ss": (azaza(bs=[set]), set()),
        "v-e-sx-sx": (azaza(bs=[set]), azaza(bs=[set])),
        "v-n-ff-ff": (frozenset("ab"), frozenset("cd")),
        "v-n-ff-fx": (frozenset("ab"), azaza("cd", bs=[frozenset])),
        "v-n-ff-ss": (frozenset("ab"), set("cd")),
        "v-n-ff-sx": (frozenset("ab"), azaza("cd", bs=[set])),
        "v-n-fx-ff": (azaza("ab", bs=[frozenset]), frozenset("cd")),
        "v-n-fx-fx": (
            azaza("ab", bs=[frozenset]),
            azaza("cd", bs=[frozenset]),
        ),
        "v-n-fx-ss": (azaza("ab", bs=[frozenset]), set("cd")),
        "v-n-fx-sx": (azaza("ab", bs=[frozenset]), azaza("cd", bs=[set])),
        "v-n-ss-ff": (set("ab"), frozenset("cd")),
        "v-n-ss-fx": (set("ab"), azaza("cd", bs=[frozenset])),
        "v-n-ss-ss": (set("ab"), set("cd")),
        "v-n-ss-sx": (set("ab"), azaza("cd", bs=[set])),
        "v-n-sx-ff": (azaza("ab", bs=[set]), frozenset("cd")),
        "v-n-sx-fx": (azaza("ab", bs=[set]), azaza("cd", bs=[frozenset])),
        "v-n-sx-ss": (azaza("ab", bs=[set]), set("cd")),
        "v-n-sx-sx": (azaza("ab", bs=[set]), azaza("cd", bs=[set])),
    }.items()
]


unhappy_data = [
    pytest.param(arg1, arg2, id=name)
    for name, (arg1, arg2) in {
        "type-0-1": (set(), azaza()),
        "type-1-0": (azaza(), set()),
        "type-1-1": (azaza(), azaza()),
    }.items()
]
