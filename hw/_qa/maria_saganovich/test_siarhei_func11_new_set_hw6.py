from hw.siarhei_apanel.refakt import new_set


def test_func11_new_set() -> None:
    result = new_set({""}, [])
    errors = result.get("errors")
    assert type(errors) == list
    assert errors == sorted(errors)
