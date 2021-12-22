from hw.vlad_yancharski.func_dom import f1, f2, f3, f4, f5


def test_12() -> None:
    assert f1() is True
    assert f2() is False
    assert f3() is None  # type: ignore
    assert f4() < 0
    assert f5() == ""
