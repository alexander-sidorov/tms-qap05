from hw.valeriya_mavritskaya.functions_lesson04 import five
from hw.valeriya_mavritskaya.functions_lesson04 import four
from hw.valeriya_mavritskaya.functions_lesson04 import one
from hw.valeriya_mavritskaya.functions_lesson04 import three
from hw.valeriya_mavritskaya.functions_lesson04 import two


def test_one() -> None:
    assert one() is True


def test_two() -> None:
    assert two() is False


def test_three() -> None:
    assert three() is None  # type: ignore


def test_four() -> None:
    assert four() < 0


def test_five() -> None:
    assert five() == ""
