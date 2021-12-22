from hw.andrei_bondar.test_bondar32 import f, g


def test_rwfwfw() -> None:
    assert f() is None  # type: ignore
    assert g() == 4
