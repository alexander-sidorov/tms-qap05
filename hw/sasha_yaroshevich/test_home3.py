from hw.sasha_yaroshevich.home3_funk import f
from hw.sasha_yaroshevich.home3_funk import fu
from hw.sasha_yaroshevich.home3_funk import fun
from hw.sasha_yaroshevich.home3_funk import func
from hw.sasha_yaroshevich.home3_funk import funct


def test_home3() -> None:
    assert func() is True
    assert funct() is False
    assert fun() is None  # type: ignore
    assert fu() < 0
    assert f() == ""
