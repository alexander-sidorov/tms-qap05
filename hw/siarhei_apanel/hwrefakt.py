def func(a1: float, back: float, cill: float) -> list:
    disk = back ** 2 - 4 * a1 * cill
    sqrt = disk ** 0.5

    x1 = (-back + sqrt) / 2 * a1
    x2 = (-back - sqrt) / 2 * a1
    return [x1, x2]


def f() -> None:
    4  # noqa: B018


def g() -> int:
    return 4
