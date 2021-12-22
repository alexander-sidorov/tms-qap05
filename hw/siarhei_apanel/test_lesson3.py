from hw.siarhei_apanel.refakt import far, gar


def test_func() -> None:
    assert far() is None  # type: ignore
    assert gar() == 4
