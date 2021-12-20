def d() -> bool:
    return True


def e() -> bool:
    return False


def n() -> int:
    return -1


def i() -> None:
    pass


def s() -> str:
    return ""


def denis() -> None:
    assert d() is True
    assert e() is False
    assert n() < 0
    assert i() is None  # type: ignore
    assert s() == ""
