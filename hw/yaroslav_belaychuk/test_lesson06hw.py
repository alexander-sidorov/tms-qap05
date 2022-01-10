from hw.yaroslav_belaychuk.lesson06hw import collection
from hw.yaroslav_belaychuk.lesson06hw import cortage
from hw.yaroslav_belaychuk.lesson06hw import str_in_str
from hw.yaroslav_belaychuk.lesson06hw import string
from hw.yaroslav_belaychuk.lesson06hw import string_zaglavie


def test_function() -> None:
    assert (cortage([1, 2, 3, 8, 65, 99])) == (1, 99)
    assert (string("ping pong")) == "pong ping"
    assert (collection([20, 100, "cola", 60], "cola")) == [20, 100, "cola"]
    assert (str_in_str("abc", "*")) == "a*b*c"
    assert (string_zaglavie("alTaVIsTA")) == "Altavista"
