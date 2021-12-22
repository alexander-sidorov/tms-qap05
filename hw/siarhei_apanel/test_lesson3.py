from refakt import far
from refakt import gar


def test_func() -> None:
    assert far() is None  # type: ignore
    assert gar() == 4
