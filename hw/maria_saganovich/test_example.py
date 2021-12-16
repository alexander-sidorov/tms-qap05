def test_example() -> None:
    assert True, "not True"
    assert (100 + 2) == 102
    num1  = 3
    num2 = 5
    result = num1 if num1 > num2 else num2
    assert result != 1
    str1 = "South"
    str2 = "Korea"
    assert (str1 + " " + str2) == "South Korea"
    assert str[1:4] == "out"
