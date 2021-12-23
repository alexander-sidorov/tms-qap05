from hw.andrey_yelin.functions_l04 import fuc, fua, fub, fud, fue


def test() -> None:
    assert fua() is True
    assert fub() is False
    assert fuc() is None  # type: ignore
    assert fud() < 0
    assert fue() == ""
