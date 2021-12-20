def f() -> None:
    4  # noqa


def g() -> int:
    return 4


def test_f() -> None:
    assert f() is None  # type: ignore
    assert g() == 4
