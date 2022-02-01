from types import FunctionType
from types import ModuleType

import pytest

from hw._qa.hw10.common import get_class
from hw.alexander_sidorov.lesson10 import homework as alexander_sidorov
from hw.andrey_yelin.lesson06 import functions_lesson06hw as andrey_yelin
from hw.maria_saganovich import final as maria_saganovich
from hw.siarhei_apanel import class10hw as siarhei_apanel
from hw.vadim_maletski import func6 as vadim_maletski

modules = {
    alexander_sidorov,
    andrey_yelin,
    maria_saganovich,
    siarhei_apanel,
    vadim_maletski,
}


@pytest.mark.parametrize("module", modules)
def test_level_01(module: ModuleType) -> None:
    cls = get_class(
        module,
        "Palindrome01",
        expected_attrs_types={
            "__bool__": FunctionType,
            "__init__": FunctionType,
        },
        expected_public_attrs=False,
    )

    assert cls("")
    assert cls("x")
    assert cls("xx")
    assert cls("xxx")
    assert not cls("xx x")
    assert not cls("xX")
    assert not cls("xy")
