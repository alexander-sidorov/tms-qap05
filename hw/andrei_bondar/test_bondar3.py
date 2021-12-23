from hw.andrei_bondar.bondar3 import f
from hw.andrei_bondar.bondar3 import g


def test_rwfwfw() -> None:
    assert f() is None  # type: ignore
    assert g() == 4
