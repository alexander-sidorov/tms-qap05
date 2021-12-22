from hw.denis_asipenko.func_da_hw import d
from hw.denis_asipenko.func_da_hw import e
from hw.denis_asipenko.func_da_hw import i
from hw.denis_asipenko.func_da_hw import n
from hw.denis_asipenko.func_da_hw import s


def test_denis() -> None:
    assert d() is True
    assert e() is False
    assert n() is None  # type: ignore
    assert i() < 0
    assert s() == ""
