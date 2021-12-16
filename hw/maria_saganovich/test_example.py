def test_example() -> None:
    assert True, "not True"
    num1 = 3
    num2 = 5
    num3 = 100
    num4 = 2
    str1 = "South"
    str2 = "Korea"
    assert (num3 + num4 == 102)
    result = num1 if num1 > num2 else num2
    assert result != 1
    assert (str1 + " " + str2 == "South Korea")
    assert str1[1:4] == "out"
