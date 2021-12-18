def g() -> None:
    4  # noqa: B018


def test_ui() -> None:
    assert g() is None  # type: ignore
