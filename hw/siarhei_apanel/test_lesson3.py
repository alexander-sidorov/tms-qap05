from test_refakt import far
from test_refakt import gar


def test_func() -> None:
    assert far() is None  # type: ignore
    assert gar() == 4
