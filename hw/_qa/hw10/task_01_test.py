from types import FunctionType
from types import ModuleType

import pytest

from hw._qa.hw10.common import get_class
from hw.alexander_sidorov.lesson10 import homework as alexander_sidorov
from hw.kirill_tobolich import lesson10_hw as kirill_tobolich

modules = {
    alexander_sidorov,
    kirill_tobolich,
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
