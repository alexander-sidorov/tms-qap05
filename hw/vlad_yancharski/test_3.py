from hw.vlad_yancharski.func_3 import f1
from hw.vlad_yancharski.func_3 import g2

def test_f1() -> None:
    assert f1() is None  # type: ignore
    assert g2() == 4
