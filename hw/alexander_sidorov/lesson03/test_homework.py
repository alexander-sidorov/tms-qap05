from cmath import isnan

import pytest

from hw.alexander_sidorov.lesson03.homework import Complex
from hw.alexander_sidorov.lesson03.homework import empty_text
from hw.alexander_sidorov.lesson03.homework import false
from hw.alexander_sidorov.lesson03.homework import nan
from hw.alexander_sidorov.lesson03.homework import negative
from hw.alexander_sidorov.lesson03.homework import none
from hw.alexander_sidorov.lesson03.homework import quadratic_roots
from hw.alexander_sidorov.lesson03.homework import true


def test_true() -> None:
    assert true() == True  # noqa: E712  # pylint: disable=singleton-comparison
    assert true() is True


def test_false() -> None:
    assert not false()
    assert false() is False


def test_none() -> None:
    assert not none()  # type: ignore
    assert none() is None  # type: ignore


def test_negative() -> None:
    assert negative()
    assert negative() < 0


def test_empty_text() -> None:
    assert not empty_text()
    assert empty_text() == ""


@pytest.mark.parametrize(
    "a,b,c,x1,x2,description",
    [
        (0, 0, 0, 0, 0, "tautology: 0 = 0"),
        (0, 0, 1, nan, nan, "no solution: c = 0"),
        (0, 2, 0, 0, 0, "linear degenerate: bx = 0"),
        (0, 2, 1, -1 / 2, -1 / 2, "linear: bx + c = 0"),
        (2, 0, 0, 0, 0, "parabolic degenerate: axx = 0"),
        (2, 0, -2, 1, -1, "parabolic real: axx + c = 0"),
        (2, 0, 2, 1j, -1j, "parabolic imaginary: axx + c = 0"),
        (2, 1, 0, 0, -1 / 2, "affine: axx + bx = 0"),
        (
            2,
            2,
            5,
            -1 / 2 + 3j / 2,
            -1 / 2 - 3j / 2,
            "square complex: axx + bx + c = 0",
        ),
        (2, 4, 2, -1, -1, "square degenerate: axx + bx + c = 0"),
        (2, 5, 2, -1 / 2, -2, "square real: axx + bx + c = 0"),
    ],
)
# pylint: disable=invalid-name
def test_quadratic_roots(
    a: Complex,  # noqa: VNE001
    b: Complex,  # noqa: VNE001
    c: Complex,  # noqa: VNE001
    x1: Complex,
    x2: Complex,
    description: str,
) -> None:
    r1, r2 = quadratic_roots(a, b, c)

    error_message = (
        f"{description} failed\n"
        f"\t{a = }\n"
        f"\t{b = }\n"
        f"\t{c = }\n"
        f"expected\n"
        f"\t{x1 = }\n"
        f"\t{x2 = }\n"
        f"got\n"
        f"\t{r1 = }\n"
        f"\t{r2 = }\n"
    )

    ok1 = (x1 == pytest.approx(r1)) or (isnan(x1) and isnan(r1))
    ok2 = (x2 == pytest.approx(r2)) or (isnan(x2) and isnan(r2))
    ok = ok1 and ok2

    assert ok, error_message
