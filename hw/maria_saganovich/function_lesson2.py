def func1() -> int:
    num1 = 7
    num2 = 2
    result1 = num1 % num2  # noqa: S001
    return result1


def func2() -> float:
    num4 = 10 / 3
    return num4


def func3() -> int:
    num5 = 10
    result2 = num5 ** 10
    return result2


def func4() -> str:
    str1 = "Busan"
    return str1
