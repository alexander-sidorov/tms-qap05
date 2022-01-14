from hw.siarhei_apanel.refakt import repeat


def test_func5_repeat() -> None:
    c1: list = []
    result1 = repeat(c1)
    errors = result1.get("errors")
    assert isinstance(errors, list)
    assert errors == sorted(errors)
