def func() -> True:
    return True


def funct() -> False:
    return False


def fun() -> None:
    pass


def fu() -> int:
    return -4


def f() -> str:
    return ""


def test_home3() -> None:
    assert func() is True  # type: ignore
    assert funct() is False  # type: ignore
    assert fun() is None  # type: ignore
    assert fu() < 0
    assert f() == ""
