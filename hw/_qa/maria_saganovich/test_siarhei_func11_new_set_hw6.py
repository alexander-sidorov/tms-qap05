from hw.siarhei_apanel.refakt import new_set


def test_func11_new_set() -> None:
    result = new_set({""}, [])
    errors = result.get("errors")
<<<<<<< HEAD
=======
    assert isinstance(errors, list)
>>>>>>> main
    assert errors == sorted(errors)
