from hw.maria_saganovich.test_agression_hw.agression import aggression


def test_aggression1() -> None:
    assert aggression(True) == "оно и видно!"
    assert aggression(False) == "а могли бы и знать!"
