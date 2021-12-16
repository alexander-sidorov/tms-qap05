def test_example() -> None:
    assert True, "not True"
    num1 = 7
    num2 = 2
    num3 = 3
    num4 = 10 / 3
    num5 = 10
    str1 = "Busan"
    result = num1 % num2
    assert result != 0
    assert num4 > 3
    assert num5 ** 10 != 10
    assert str1 == "Busan"
    assert num1 != 3
    assert num1 - num2 == 5
    num3 *= 3
    assert num3 != 5
