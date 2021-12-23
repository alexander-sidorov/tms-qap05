from hw.andrei_bondar.bondar3hw import a
from hw.andrei_bondar.bondar3hw import b
from hw.andrei_bondar.bondar3hw import c
from hw.andrei_bondar.bondar3hw import d
from hw.andrei_bondar.bondar3hw import e


def test() -> None:
    assert a() is True
    assert b() is False
    assert c() is None  # type: ignore
    assert d() < 0
    assert e() == ""
