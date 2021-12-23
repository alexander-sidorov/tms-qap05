from hw.vadim_maletski.func import func_answer


def test() -> None:
    assert func_answer("Да") == "Оно и видно"
    assert func_answer("Нет") == "А могли бы знать"
    assert func_answer("") == "Ответьте 'Да' или 'Нет'"
