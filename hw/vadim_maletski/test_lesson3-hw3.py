def func1() -> bool:
    python = True
    return python


def func2() -> bool:
    not_python = False
    return not_python


def func3() -> None:
    pass


def func4() -> int:
    num1 = 5
    num2 = 6
    num3 = num1 - num2
    return num3


def func5() -> str:
    str1 = ""
    return str1


def kv_ur(num1, num2, num3) -> list:
    dis = round((num2 ** 2 - 4 * num1 * num3), 2)

    if dis >= 0:
        x1 = round(((-num2 + dis ** 0.5) / 2 * num1), 2)
        x2 = round(((-num2 - dis ** 0.5) / 2 * num1), 2)

    else:
        x1 = None
        x2 = None

    return x1, x2


def test() -> None:
    assert func1() is True
    assert func2() is False
    assert func3() is None
    assert func4() < 0
    assert func5() == ""
    assert kv_ur(1, 2, 1) == (-1.0, -1.0)
    assert kv_ur(1, 1, 1) == (None, None)
