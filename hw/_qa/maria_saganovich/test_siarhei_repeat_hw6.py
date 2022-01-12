from hw.siarhei_apanel.refakt import repeat


<<<<<<< HEAD
def test_func5_repeat():
    c1: list = []
    result1 = repeat(c1)
    errors = result1.get("errors")
=======
def test_func5_repeat() -> None:
    c1: list = []
    result1 = repeat(c1)
    errors = result1.get("errors")
    assert isinstance(errors, list)
>>>>>>> main
    assert errors == sorted(errors)
