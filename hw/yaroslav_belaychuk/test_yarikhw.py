def fnc(num1: float, num2: float, num3: float) -> list:
    dsk = num2 ** 2 - 4 * num1 * num3
    kordsk = dsk ** 0.5
    if dsk > 0:
        x1 = -num2 + kordsk / 2 * num1
        x2 = -num2 - kordsk / 2 * num1
        return [x1, x2]
    elif dsk == 0:
        x3 = -num2 + kordsk / 2 * num1
        return [x3]
    else:
        return [None]


def test_f() -> None:
    assert fnc(1, 4, 9) == [0, -1]
    assert fnc(1, 1, 1) == [0, -1]
    assert fnc(1, 2, 1) == [0, -1]
