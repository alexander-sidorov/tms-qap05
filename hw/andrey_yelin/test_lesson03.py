def f() -> None:
    4 # noqa: B018



def g() -> int:
    return 4



def test_ddfdd(): -> None:
    assert f() is None # tupe: ignore
    assert g() == 4
 
