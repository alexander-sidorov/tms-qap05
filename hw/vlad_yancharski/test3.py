def f() -> None:
    5 # type: ignore


def test_f() -> None:
    assert f() is None  # type: ignore
