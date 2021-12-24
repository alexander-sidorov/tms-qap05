from hw.alexander_sidorov.lesson04.homework import aggression


def test_aggression() -> None:
    assert aggression(True) == "оно и видно"
    assert aggression(False) == "а мог бы и знать"
