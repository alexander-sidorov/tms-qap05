from hw.siarhei_apanel.refakt import repeat


def test_func5_repeat() -> None:
    c1: list = []
    c2 = ["may", "day"]
    assert repeat(c1) == {
        "errors": ["arg shouldn't be empty"]
    }
    assert repeat(c2) == {"data": ["no duplicates"]}
