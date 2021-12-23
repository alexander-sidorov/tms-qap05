from hw.denis_asipenko.func_ada_lesson3 import f
from hw.denis_asipenko.func_ada_lesson3 import g


def test_ada_lesson3() -> None:
    assert f() is None  # type: ignore
    assert g() == 4
