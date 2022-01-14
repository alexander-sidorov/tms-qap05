from hw.maria_saganovich.lesson5.task5 import func5


def test_function5() -> None:
    str1 = "santa   claus is coming to town"
    assert func5(str1) == "Santa   Claus Is Coming To Town"
