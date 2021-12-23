from hw.kirill_tobolich.lesson3 import f
from hw.kirill_tobolich.lesson3 import g


def test_function() -> None:
    assert f() is None  # type: ignore
    assert g() == 4
