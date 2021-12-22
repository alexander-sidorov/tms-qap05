from hw.vadim_maletski.test_testlesson4 import func1, func2, func3, func4, func5, kv_ur


def test() -> None:
    assert func1() is True
    assert func2() is False
    assert func3() is None  # type: ignore
    assert func4() < 0
    assert func5() == ""
    assert kv_ur(1, -2, -3) == [3.0, -1.0]
    assert kv_ur(1, 2, 1) == [-1.0, -1.0]
    assert kv_ur(1, 1, 1) == [(-0.5 + 0.87j), (-0.5 - 0.87j)]
