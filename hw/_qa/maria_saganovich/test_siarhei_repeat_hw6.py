from hw.siarhei_apanel.refakt import repeat


def test_func5_repeat():
    c1: list = []
    result1 = repeat(c1)
    errors = result1.get("errors")
    assert errors == sorted(errors)
