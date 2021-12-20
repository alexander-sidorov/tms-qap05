def d() -> bool:
    return True


def e() -> bool:
    return False


def n() -> int:
    return -26


def i() -> None:
    pass


def s() -> str:
    return ""


def denis() -> None:
    assert d(" + ")
    assert e(5 - 5 == 1)
    assert n() < 0
    assert i() is None  # type: ignore
    assert s() == ""
