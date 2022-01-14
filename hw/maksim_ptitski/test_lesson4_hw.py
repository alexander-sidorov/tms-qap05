from hw.maksim_ptitski.lesson4_hw import aggression


def test_example() -> None:
    assert aggression(True) == "Оно и видно"
    assert aggression(False) == "А могли бы знать"
