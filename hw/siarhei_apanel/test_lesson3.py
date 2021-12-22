from hwrefakt import f
from hwrefakt import g


def test_func() -> None:
    assert f() is None  # type: ignore
    assert g() == 4
