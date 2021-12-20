def func(a1: float, back: float, cill: float) -> list:
    if a1 == 0:
        return [None, None]
    disk = back ** 2 - 4 * a1 * cill
    sqrt = disk ** (0.5)
    if disk >= 0:
        x1 = (-back + sqrt) / 2 * a1
        x2 = (-back - sqrt) / 2 * a1
        return [x1, x2]
    else:
        return [None, None]


def test() -> None:
    assert func(1, 2, 1) == [-1.0, -1.0]
    assert func(1, 1, 1) == [None, None]
