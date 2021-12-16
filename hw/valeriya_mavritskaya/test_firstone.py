def test_example() -> None:
    assert True, "not True"
    assert 1 + 2 == 3
    assert True is True
    assert False == 0  # noqa: SIM300,E712
    assert "22" == "22"  # noqa: SIM300
    assert "2" + "2" == "22"
