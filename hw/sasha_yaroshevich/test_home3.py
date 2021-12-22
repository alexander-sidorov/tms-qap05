from hw.sasha_yaroshevich.home3_funk import func, funct, fun, fu, f


def test_home3() -> None:
    assert func() is True
    assert funct() is False
    assert fun() is None  # type: ignore
    assert fu() < 0
    assert f() == ""
