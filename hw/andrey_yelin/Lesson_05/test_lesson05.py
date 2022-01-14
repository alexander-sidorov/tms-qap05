from hw.andrey_yelin.Lesson_05.yelin_lesson05 import aggression


def test_aggression() -> None:
    assert aggression(True) == "оно и видно"
    assert aggression(False) == "а мог бы и знать"
