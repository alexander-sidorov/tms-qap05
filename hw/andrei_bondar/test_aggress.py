from hw.andrei_bondar.aggression5 import aggression


def test_aggression1() -> None:
    assert aggression(True) == "оно и видно!"
    assert aggression(False) == "а могли бы и знать!"
