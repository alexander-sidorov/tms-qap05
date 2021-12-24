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
        x1 = (-var_b + (discriminant ** 0.5)) / (2 * var_a)
        x1 = round(x1.real, 2) + round(x1.imag, 2) * 1j
        x2 = (-var_b - (discriminant ** 0.5)) / (2 * var_a)
        x2 = round(x2.real, 2) + round(x2.imag, 2) * 1j
    return [x1, x2]
