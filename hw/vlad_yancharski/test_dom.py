def f1() -> bool:
    return True


def f2() -> bool:
    return False


def f3() -> None:
    pass


def f4() -> int:
    return -3


def f5() -> str:
    return ""


def x() -> None:
    assert f1() is True
    assert f2() is False
    assert f3() is None  # type: ignore
    assert f4() < 0
    assert f5() == ""
