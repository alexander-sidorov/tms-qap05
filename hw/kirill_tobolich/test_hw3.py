import math


def func1() -> bool:
    return True


def func2() -> bool:
    return False


def func3() -> None:
    pass


def func4() -> int:
    return -5


def func5() -> str:
    return ""


def quadratic_equation(var_a, var_b, var_c) -> list:  # type: ignore
    discriminant = var_b ** 2 - 4 * var_a * var_c
    if discriminant >= 0:
        x1 = (-var_b + math.sqrt(discriminant)) / (2 * var_a)
        x2 = (-var_b - math.sqrt(discriminant)) / (2 * var_a)
    else:
        return "No solution, D < 0"  # type: ignore
    return [x1, x2]


def test_functions() -> None:
    var_a1 = 2  # CASE1 for descriminant > 0
    var_b1 = 7  # CASE1for descriminant > 0
    var_c1 = 3  # CASE1 for descriminant > 0 case1
    var_a2 = 1  # CASE2 for descriminant < 0
    var_b2 = 1  # CASE2 for descriminant < 0
    var_c2 = 1  # CASE2 for descriminant < 0
    var_a3 = 1  # CASE3 for x1 = x2
    var_b3 = 2  # CASE3for x1 = x2
    var_c3 = 1  # CASE3for x1 = x2
    case1_roots = quadratic_equation(var_a1, var_b1, var_c1)
    case1_result_with_x1 = (
        var_a1 * case1_roots[0] ** 2 + var_b1 * case1_roots[0] + var_c1
    )
    case1_result_with_x2 = (
        var_a1 * case1_roots[1] ** 2 + var_b1 * case1_roots[1] + var_c1
    )
    case2_roots = quadratic_equation(var_a2, var_b2, var_c2)
    case3_roots = quadratic_equation(var_a3, var_b3, var_c3)
    case3_result_with_x1 = (
        var_a3 * case3_roots[0] ** 2 + var_b3 * case3_roots[0] + var_c3
    )
    case3_result_with_x2 = (
        var_a3 * case3_roots[1] ** 2 + var_b3 * case3_roots[1] + var_c3
    )
    assert func1() is True
    assert func2() is False
    assert func3() is None  # type: ignore
    assert func4() < 0
    assert func5() == ""
    assert case1_result_with_x1 == 0
    assert case1_result_with_x2 == 0
    assert case2_roots == "No solution, D < 0"
    assert case3_roots[0] == case3_roots[1]
    assert case3_result_with_x1 == 0
    assert case3_result_with_x2 == 0
