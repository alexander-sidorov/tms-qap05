from hw.kirill_tobolich.lesson_04_hw2 import aggression


def test_example() -> None:
    assert aggression(True) == "Оно и видно"
    assert aggression(False) == "А могли бы знать"
