from hw.denis_asipenko.hw_lesson5 import aggression


def test_homework5() -> None:
    assert aggression(True) == "оно и видно"
    assert aggression(False) == "а мог бы и знать"
