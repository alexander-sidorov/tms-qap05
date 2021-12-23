from hw.andrey_yelin.functions_l04 import fua
from hw.andrey_yelin.functions_l04 import fub
from hw.andrey_yelin.functions_l04 import fuc
from hw.andrey_yelin.functions_l04 import fud
from hw.andrey_yelin.functions_l04 import fue


def test() -> None:
    assert fua() is True
    assert fub() is False
    assert fuc() is None  # type: ignore
    assert fud() < 0
    assert fue() == ""
