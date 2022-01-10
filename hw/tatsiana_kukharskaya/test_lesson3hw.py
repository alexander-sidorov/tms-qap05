def avr1() -> bool:
    return True


def avr2() -> bool:
    return False


def kim() -> int:
    return -8


def k() -> None:
    7  # noqa: B018


def den() -> str:
    return ""


def test_alle() -> None:
    assert avr1() is True
    assert avr2() is False
    assert kim() < 0
    assert k() is None  # type: ignore
    assert den() == ""
