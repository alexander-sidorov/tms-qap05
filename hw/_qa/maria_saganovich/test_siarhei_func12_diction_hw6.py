from hw.siarhei_apanel.refakt import diction


def test_func12_diction() -> None:
    assert diction(1, 2, 3, 4, 5, 7, 6, 9) == {
        "data": {1: 2, 3: 4, 5: 6, 7: None, 9: None}
    }
    assert diction(1, 2, 3, 4, 5, 6, 8, 10) == {
        "data": {1: 2, 3: 4, 5: 6, ...: [8, 10]}
    }
    assert diction(1, "", 3, 4) == {
        "errors": ["should be number"]
    }
    assert diction(1, 2, 3, 4, 5, 6, 8) == {
        "data": {1: 2, 3: 4, 5: 6, ...: [8]}
    }
