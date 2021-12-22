from hw.maria_saganovich.function_lesson2 import func1, func2, func3, func4


def test_example() -> None:
    assert True, "not True"
    assert func1() != 0
    assert func2() > 3
    assert func3() != 10
    assert func4() == "Busan"
