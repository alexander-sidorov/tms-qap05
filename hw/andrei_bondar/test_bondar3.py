from hw.andrei_bondar.test_bondar32 import f
from hw.andrei_bondar.test_bondar32 import g


def test_rwfwfw() -> None:
    assert f() is None  # type: ignore
    assert g() == 4
