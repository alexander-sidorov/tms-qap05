from hw.maria_saganovich.lesson5.task1 import func1


def test_func1() -> None:
    list1 = ["New", "Happy", "Christmas", "Year"]
    assert func1(list1) == ("New", "Year")
