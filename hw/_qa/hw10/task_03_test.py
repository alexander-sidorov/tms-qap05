from types import FunctionType
from types import ModuleType

import pytest

from hw._qa.hw10.common import get_class
from hw.alexander_sidorov.lesson10 import homework as alexander_sidorov
from hw.andrey_yelin.lesson06 import functions_lesson06hw as andrey_yelin
from hw.siarhei_apanel import class10hw as siarhei_apanel
from hw.vadim_maletski import func6 as vadim_maletski

modules = {
    alexander_sidorov,
    andrey_yelin,
    siarhei_apanel,
    vadim_maletski,
}


@pytest.mark.parametrize("module", modules)
def test_level_03(module: ModuleType) -> None:
    cls = get_class(
        module,
        "HttpQuery03",
        expected_attrs_types={
            "__getitem__": FunctionType,
            "__init__": FunctionType,
        },
        expected_public_attrs=False,
    )

    obj = cls("x=1&y=2&y=3")
    assert obj["x"] == "1"
    assert obj["y"] == ["2", "3"]
    assert obj["z"] is None

    obj = cls("x=1&y=2&y=")
    assert obj["x"] == "1"
    assert obj["y"] == ["2", ""]
    assert obj["z"] is None
