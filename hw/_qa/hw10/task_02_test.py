from datetime import date
from types import FunctionType
from types import ModuleType

import pytest

from hw._qa.hw10.common import get_class
from hw.alexander_sidorov.lesson10 import homework as alexander_sidorov
from hw.siarhei_apanel.refakt import User02 as siarhei_apanel
modules = {
    alexander_sidorov,
    siarhei_apanel,
}


@pytest.mark.parametrize("module", modules)
def test_level_02(module: ModuleType) -> None:
    cls = get_class(
        module,
        "User02",
        expected_attrs_types={
            "__init__": FunctionType,
            "age": property,
        },
    )

    today = date.today()
    birthday = date(today.year - 10, 1, 1)

    assert cls(birthday).age == 10
