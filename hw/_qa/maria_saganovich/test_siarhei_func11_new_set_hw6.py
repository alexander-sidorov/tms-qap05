from hw.siarhei_apanel.refakt import new_set


def test_func11_new_set() -> None:
    assert new_set({""}, []) == {  # noqa: JS101
        "errors": ["arg should be set"]
    }  # noqa: JS102
