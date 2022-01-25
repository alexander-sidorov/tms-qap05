def test_example() -> None:
    assert True, "not True"
    assert 0 ** 0 == 1
    assert (True + True) == 2
    assert "" + "" == ""

    assert True == True  # noqa: E712,SIM300  # pylint: disable=R0124,C0121
