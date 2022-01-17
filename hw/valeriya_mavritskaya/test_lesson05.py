from hw.valeriya_mavritskaya.lesson05_functions import lvl_1
from hw.valeriya_mavritskaya.lesson05_functions import lvl_2
from hw.valeriya_mavritskaya.lesson05_functions import lvl_3
from hw.valeriya_mavritskaya.lesson05_functions import lvl_4
from hw.valeriya_mavritskaya.lesson05_functions import lvl_5


def test_lvl_1() -> None:
    collection = [1, 2, 3, 66, 4, 5, 6]
    assert lvl_1(collection) == (1, 6)


def test_lvl_2() -> None:
    phrase = "two words"
    assert lvl_2(phrase) == "words two"


def test_lvl_3() -> None:
    collection3 = (1, 2, 3, 66, 4, 5, 6)
    object3 = 66
    assert lvl_3(collection3, object3) == (1, 2, 3, 66)


def test_lvl_4() -> None:
    some_string = "val"
    symbol = "*"
    assert lvl_4(some_string, symbol) == "v*a*l"


def test_lvl_5() -> None:
    string_to_be_capitalized = "nice to meet you"
    assert lvl_5(string_to_be_capitalized) == "Nice To Meet You"
