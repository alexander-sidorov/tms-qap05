from datetime import date
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
