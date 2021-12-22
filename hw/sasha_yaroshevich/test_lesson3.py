from hw.sasha_yaroshevich.lesson3_fink2 import f
from hw.sasha_yaroshevich.lesson3_fink2 import g


def test_lesson3() -> None:
    assert f() is None  # type: ignore
    assert g() == 4
