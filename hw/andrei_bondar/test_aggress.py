from hw.andrei_bondar.aggression5 import aggression


def test_aggression5() -> None:
    assert aggression(True) == "оно и видно"
    assert aggression(False) == "а мог бы и знать"
