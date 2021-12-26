from hw.vadim_maletski.func import func_answer


def test() -> None:
    assert func_answer(True) == "Оно и видно "
    assert func_answer(False) == "А могли бы знать "
