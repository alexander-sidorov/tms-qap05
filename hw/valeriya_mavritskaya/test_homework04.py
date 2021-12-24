from hw.valeriya_mavritskaya.homework04 import aggression


def test_homework04() -> None:
    assert aggression(True) == "оно и видно"
    assert aggression(False) == "а мог бы и знать"
