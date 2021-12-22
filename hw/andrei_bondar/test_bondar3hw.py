from hw.andrei_bondar.test_bondar32hw import a, b, c, d, e


def test() -> None:
    assert a() is True
    assert b() is False
    assert c() is None  # type: ignore
    assert d() < 0
    assert e() == ""
