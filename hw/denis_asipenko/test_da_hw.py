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
    assert func() is True
    assert funct() is False
    assert fun() is None  # type: ignore
    assert fu() < 0
    assert f() == ""
