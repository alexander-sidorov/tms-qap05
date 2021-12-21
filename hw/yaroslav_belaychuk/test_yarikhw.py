def fnc(num1: float, num2: float, num3: float) -> list:
    dsk = num2 ** 2 - 4 * num1 * num3
    kordsk = dsk ** 0.5
    x1 = -num2 + kordsk / 2 * num1
    x2 = -num2 - kordsk / 2 * num1
    return [x1, x2]


def test_f() -> None:
    assert fnc(1, 4, 9) == [(-4 + 2.23606797749979j), (-4 - 2.23606797749979j)]
    assert fnc(1, 1, 1) == [
        (-1 + 0.8660254037844386j),
        (-1 - 0.8660254037844386j),
    ]
    assert fnc(1, 2, 1) == [-2.0, -2.0]
