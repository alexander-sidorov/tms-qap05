def func(a1: float, back: float, cill: float) -> float:
    if a1 == 0:
        return None
    disk = back ** 2 - 4 * a1 * cill
    sqrt = disk ** (0.5)
    if disk > 0:
        x1 = (-back + sqrt) / 2 * a1
        x2 = (-back - sqrt) / 2 * a1
        return x1, x2
    elif disk == 0:
        xone = (-back + sqrt) / 2 * a1
        return xone
    else:
        return None

def test() -> None:
    func(1, 2, 1) == -1.0
