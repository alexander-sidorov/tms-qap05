# Выбирете ответ на предложенный вопрос и вызовете фунцию
from hw.siarhei_apanel.refakt import vopros

question = "Знаете, что такое пассивная агрессия?"

answerYES = "Да"  # noqa N816
answerNO = "Нет"  # noqa N816


def test() -> None:
    assert vopros(question, answerYES) == "Оно и видно!"
    assert vopros(question, answerNO) == "А могли бы и знать!"
