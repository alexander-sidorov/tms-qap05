import pytest

from hw.siarhei_apanel import refakt as hw05


@pytest.mark.xfail
def test_lesson_05_hw() -> None:
    assert hw05.srez([1, 2, 3, 4], 3) == [1, 2, 3]
