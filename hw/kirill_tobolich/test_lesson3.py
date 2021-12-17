def f() -> None:
    4  # noqa: B018


def g() -> int:
    return 4


def test_function() -> None:
    assert f() is None  # type: ignore
    assert g() == 4
