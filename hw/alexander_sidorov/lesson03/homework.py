from typing import Any
from typing import Tuple
from typing import Union


def true() -> Any:
    return True


def false() -> bool:
    return False


def none() -> None:
    return None


def negative() -> int:
    return -1


def empty_text() -> str:
    return ""


Complex = Union[int, float, complex]

nan = complex("nan")


# pylint: disable=invalid-name
def quadratic_roots(
    a: Complex,  # noqa: VNE001
    b: Complex,  # noqa: VNE001
    c: Complex,  # noqa: VNE001
) -> Tuple[Complex, Complex]:
    a = complex(a)  # noqa: VNE001
    b = complex(b)  # noqa: VNE001
    c = complex(c)  # noqa: VNE001

    x1: Complex
    x2: Complex

    if a == 0:
        # degenerate cases
        if b == 0:
            if c == 0:
                x1 = x2 = 0
            else:
                x1 = x2 = nan
        else:
            x1 = x2 = -c / b
    else:
        d = (b**2 - 4 * a * c) ** 0.5  # noqa: VNE001
        a2 = 2 * a
        x1 = (-b + d) / a2
        x2 = (-b - d) / a2

    x1 = complex(x1)
    x2 = complex(x2)

    return x1, x2
