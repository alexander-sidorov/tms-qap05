def f() -> None:
    4


def g() -> int:
    return 4


def test_function():
    assert f() is None
    assert g() == 4
