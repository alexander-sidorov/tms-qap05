def func() -> bool:
    return True


def funct() -> bool:
    return False


def fun() -> None:
    pass


def fu() -> int:
    return -4


def f() -> str:
    return ""


def test_home3() -> None:
    assert func() is True
    assert funct() is False
    assert fun() is None  # type: ignore
    assert fu() < 0
    assert f() == ""
