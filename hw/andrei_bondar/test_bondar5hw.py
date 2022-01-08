from hw.andrei_bondar.bondar5hw import fun1
from hw.andrei_bondar.bondar5hw import fun2
from hw.andrei_bondar.bondar5hw import fun3
from hw.andrei_bondar.bondar5hw import fun4
from hw.andrei_bondar.bondar5hw import fun5


def test_fun1() -> None:
    collection = [1, 2, 3, 4, 5, 10]
    assert fun1(collection) == (1, 10)


def test_fun2() -> None:
    string1 = "home work"
    assert fun2(string1) == "work home"


def test_fun3() -> None:
    collection1 = (1, 2, 3, 4, 5, 10)
    object3 = 4
    assert fun3(collection1, object3) == (1, 2, 3, 4)


def test_fun4() -> None:
    string1 = "blabla"
    string_v_1 = "o"
    assert fun4(string1, string_v_1) == "boloaoboloa"


def test_fun5() -> None:
    string5 = "pRoiZvolnAi sTroKa"
    assert fun5(string5) == "Proizvolnai Stroka"
