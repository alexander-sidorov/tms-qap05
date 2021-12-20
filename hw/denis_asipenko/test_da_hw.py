def d() -> bool:
    return True


def e() -> bool:
    return False


def n() -> None:
    return


def i() -> int:
    return -3


def s() -> str:
    return ""


def test_denis() -> None:
    assert d() is True
    assert e() is False
    assert n() is None  # type: ignore
    assert i() < 0
    assert s() == ""
