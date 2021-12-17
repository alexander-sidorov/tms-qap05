def test_1() -> None:
    4  # noqa: B018


def g() -> int:
    return 4


def f() -> None:
    assert f() is None  # type: ignore
    assert g() == 4
