import math


def func1() -> True:
    return True


def func2() -> False:
    return False


def func3() -> None:
    pass


def func4() -> int:
    return -5


def func5() -> str:
    return ""


def quadratic_equation(var_a, var_b, var_c) -> list:
    discriminant = var_b ** 2 - 4 * var_a * var_c
    x1 = (-var_b + math.sqrt(discriminant)) / (2 * var_a)
    x2 = (-var_b - math.sqrt(discriminant)) / (2 * var_a)
    return [x1, x2]


def test_functions() -> None:
    var_a = 2
    var_b = 7
    var_c = 3
    result_with_x1 = (
        var_a * quadratic_equation(var_a, var_b, var_c)[0] ** 2
        + var_b * quadratic_equation(var_a, var_b, var_c)[0]  # noqa: W503
        + var_c  # noqa: W503
    )
    result_with_x2 = (
        var_a * quadratic_equation(var_a, var_b, var_c)[1] ** 2
        + var_b * quadratic_equation(var_a, var_b, var_c)[1]  # noqa: W503
        + var_c  # noqa: W503
    )
    assert func1() is True
    assert func2() is False
    assert func3() is None
    assert func4() < 0
    assert func5() == ""
    assert result_with_x1 == 0
    assert result_with_x2 == 0
