import pytest

from hw._qa.hw06.common import azaza

happy_data = [  # noqa: ECE001
    pytest.param(arg, expected, id=name)
    for name, (arg, expected) in {
        "empty-x": (azaza("", bs=[str]), {}),
        "empty": ("", {}),
        "v-0-x": (azaza("xx", bs=[str]), {"xx": [""]}),
        "v-0": ("xx", {"xx": [""]}),
        "v-1": ("xx=", {"xx": [""]}),
        "v-2": ("xx=&yy=", {"xx": [""], "yy": [""]}),
        "v-3": ("xx=1&yy=2&yy=3", {"xx": ["1"], "yy": ["2", "3"]}),
        "v-4": ("xx=xx&yy=yy&yy=yy", {"xx": ["xx"], "yy": ["yy", "yy"]}),
        "v-5": ("xx=xx&yy=yy&yy=", {"xx": ["xx"], "yy": ["yy", ""]}),
    }.items()
]

unhappy_data = [
    pytest.param(arg, id=name)
    for name, arg in {
        "type": azaza(),
    }.items()
]
