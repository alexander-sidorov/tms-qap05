def f() -> None:
    4


def g() -> int:
    return 4


def test_func() -> None:
    assert f() is None
    assert g() == 4
