def func1() -> bool:
    num1 = 1
    return bool(num1 % 2 == 0)


def func2() -> bool:
    num2 = 8
    return bool(num2 % 2 == 0)


def func3() -> None:
    return


def func4() -> int:
    return -100


def func5() -> str:
    return ''


def test_functions() -> None:
    assert func1() is False
    assert func2() is True
    assert func3() is None  # type: ignore
    assert func4() == -100
    assert func5() == ""
