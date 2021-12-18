def f() -> None:
    4  # noqa: B018


def test_ui() -> None:
    assert f() is None  # type: ignore
