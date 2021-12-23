from random import random  # noqa: DUO101


def func_answer() -> int:

    ran = random()  # noqa: S311
    if ran < 0.5:
        r1 = 1
        return r1
    else:
        r2 = 0
        return r2
