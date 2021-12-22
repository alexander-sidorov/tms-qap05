from hw.kirill_tobolich.lesson3_hw import func1, func2, func3, func4, func5, quadratic_equation


def test_functions() -> None:
    assert func1() is True
    assert func2() is False
    assert func3() is None  # type: ignore
    assert func4() < 0
    assert func5() == ""
    assert quadratic_equation(2, 7, 3) == [-0.5, -3]
    assert quadratic_equation(1, 1, 1) == [(-0.5 + 0.87j), (-0.5 - 0.87j)]
    assert quadratic_equation(1, 2, 1) == [-1, -1]
