def d() -> bool:
    return True


def e() -> bool:
    return False


def n() -> None:
    return


def i() -> int:
    return -1


def s() -> str:
    return ""


def denis() -> None:
    assert d() is True
    assert e() is False
    assert n() is None  # type: ignore
    assert i() < 0
    assert s() == ""
