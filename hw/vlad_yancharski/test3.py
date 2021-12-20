def f() -> None:
    5 # noqa: B018


def test_f() -> None:
    assert f() is None  # type: ignore
