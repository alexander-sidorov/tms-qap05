import math
from typing import Any


def quadratic_equation() -> Any:
    x1: float
    x2: float
    x3: float

    print("Enter the coefficients for the equation: ")  # noqa: T001

    print("ax^2 + bx + c = 0:")  # noqa: T001
    a1 = float(input("a = "))

    if a1 == 0:
        return "'a' couldn't be = 0"

    b1 = float(input("b = "))
    c1 = float(input("c = "))

    discriminant = b1 ** 2 - 4 * a1 * c1
    print("Discriminant: D = %.1f" % discriminant)  # noqa: S001, MOD001, T001

    if discriminant > 0:
        x1 = (-b1 + math.sqrt(discriminant)) / (2 * a1)
        x2 = (-b1 - math.sqrt(discriminant)) / (2 * a1)
        print(  # noqa: S001, MOD001, T001
            f"We got the next roots: x1 = {x1:.1f}, x2 = {x2:.1f}"
        )
        return [x1, x2]
    elif discriminant == 0:
        x3 = -b1 / (2 * a1)
        print(  # noqa: S001, MOD001, T001
            "We have the next root:\nx = %.1f" % x3  # noqa: S001, MOD001, T001
        )  # noqa: S001, MOD001, T001
        return x3
    else:
        print("We have the next roots: \nNo roots")  # noqa: T001
        return False
