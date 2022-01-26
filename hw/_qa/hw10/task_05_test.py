from collections import Counter
from types import FunctionType
from types import ModuleType
from typing import Any

import pytest

from hw._qa.hw10.common import get_class
from hw.alexander_sidorov.lesson10 import homework as alexander_sidorov
from hw.siarhei_apanel import refakt as siarhei_apanel

modules = {
    alexander_sidorov,
    siarhei_apanel,
}


@pytest.mark.parametrize("module", modules)
def test_level_05(module: ModuleType) -> None:
    cls = get_class(
        module,
        "DupCounter05",
        expected_attrs_types={
            "get_dups": FunctionType,
        },
        expected_bases={Counter},
    )

    data: Any

    data = [1, 1, 1, 1, 2, 2, 3]
    obj = cls(data)
    assert obj.get_dups() == {1: 4, 2: 2}

    data = "[1, 1, 1, 1, 2, 2, 3]"
    obj = cls(data)
    assert obj.get_dups() == {
        " ": 6,
        ",": 6,
        "1": 4,
        "2": 2,
    }

    data = {1, 2, 3, 4}
    obj = cls(data)
    assert obj.get_dups() == {}

    data = range(10)
    obj = cls(data)
    assert obj.get_dups() == {}
