from hw.maksim_ptitski.lesson4_hw import passive_aggression


def test_example() -> None:
    assert passive_aggression("YES") == "Оно и видно"
    assert passive_aggression("NO") == "А могли бы знать"
