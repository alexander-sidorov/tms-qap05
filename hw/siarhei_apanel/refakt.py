def func(a1: float, back: float, cill: float) -> list:
    disk = back ** 2 - 4 * a1 * cill
    sqrt = disk ** 0.5
    x1 = (-back + sqrt) / 2 * a1
    x2 = (-back - sqrt) / 2 * a1
    return [x1, x2]


def far() -> None:
    4  # noqa: B018


def gar() -> int:
    return 4


def vopros(answer: str) -> str:
    if answer == "Да":
        return "Оно и видно!"
    elif answer == "Нет":
        return "А могли бы и знать!"
    else:
        return "Несоответствующее значение"
