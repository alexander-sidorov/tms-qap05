from hw.yaroslav_belaychuk.yarik04 import f, g


def test_func() -> None:
    assert f() is None  # type: ignore
    assert g() == 4
