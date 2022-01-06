from hw.maria_saganovich.lesson5.task4 import func4


def test_func4() -> None:
    some_string = "xxxx"
    some_string1 = "o"
    assert func4(some_string1, some_string) == "xoxoxox"
