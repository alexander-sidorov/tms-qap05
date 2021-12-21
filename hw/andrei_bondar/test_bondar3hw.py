def a() -> bool:
    return True


def b() -> bool:
    return False


def c() -> None:
    return


def d() -> int:
    return -1


def e() -> str:
    return ""


def test() -> None:
    assert a() is True
    assert b() is False
    assert c() is None  # type: ignore
    assert d() < 0
    assert e() == ""
