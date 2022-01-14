from hw.maria_saganovich.lesson5.task2 import func2


def test_func2() -> None:
    some_string = "Year New"
    assert func2(some_string) == "New Year"
