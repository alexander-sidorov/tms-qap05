from random import random  # noqa: DUO102


def func() -> str:
    if random() < 0.5:  # noqa: DUO102, S311
        return "Оно и видно!"
    else:
        return "А могли бы и знать!"
