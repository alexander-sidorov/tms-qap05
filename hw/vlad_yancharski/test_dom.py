from hw.vlad_yancharski.func_dom import f1
from hw.vlad_yancharski.func_dom import f2
from hw.vlad_yancharski.func_dom import f3
from hw.vlad_yancharski.func_dom import f4
from hw.vlad_yancharski.func_dom import f5


def test_12() -> None:
    assert f1() is True
    assert f2() is False
    assert f3() is None  # type: ignore
    assert f4() < 0
    assert f5() == ""
