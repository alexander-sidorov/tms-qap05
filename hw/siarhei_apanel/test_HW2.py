# Выбирете ответ на предложенный вопрос и вызовете фунцию
# "Знаете, что такое пассивная агрессия?"
from hw.siarhei_apanel.refakt import vopros

answer = {"YES": "Да", "NO": "Нет"}  # noqa N816
unknown = "Не знаю"  # noqa N816


def test() -> None:
    assert vopros(answer["YES"]) == "Оно и видно!"
    assert vopros(answer["NO"]) == "А могли бы и знать!"
    assert vopros(unknown) == "Несоответствующее значение"
