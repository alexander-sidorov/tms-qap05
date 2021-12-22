from hw.maria_saganovich.lesson3 import func1
from hw.maria_saganovich.lesson3 import func2


def test_1() -> None:
    assert func1() is None  # type: ignore
    assert func2() == 4
