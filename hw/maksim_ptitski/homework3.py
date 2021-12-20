def func1() -> bool:
    return True


def func2() -> bool:
    return False


def func3() -> None:
    pass


def func4() -> int:
    return -8


def func5() -> str:
    return ""


def test_function() -> None:
    assert func1() is True
    assert func2() is False
    assert func3() is None  # type: ignore
    assert func4() < 0
    assert func5() == ""
