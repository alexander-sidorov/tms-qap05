from types import FunctionType
from types import ModuleType

import pytest

from hw._qa.hw10.common import get_class
from hw.alexander_sidorov.lesson10 import homework as alexander_sidorov
from hw.maksim_ptitski import lesson10_hw as maksim_ptitski
from hw.maria_saganovich import final as maria_saganovich
from hw.siarhei_apanel import class10hw as siarhei_apanel
from hw.vadim_maletski import func6 as vadim_maletski

modules = {
    alexander_sidorov,
    maksim_ptitski,
    maria_saganovich,
    siarhei_apanel,
    vadim_maletski,
}


@pytest.mark.parametrize("module", modules)
def test_level_04(module: ModuleType) -> None:
    cls = get_class(
        module,
        "Multiplier04",
        expected_attrs_types={
            "add": FunctionType,
            "get_result": FunctionType,
        },
    )

    obj = cls().add(1).add(2).add(3)
    assert obj.get_result() == 6

    obj.add(4).add("x")
    assert obj.get_result() == "x" * 24
