from hw.siarhei_apanel.refakt import new_dict


def test_func10_new_dict() -> None:
    assert new_dict("", []) == {"errors": ["args are empty"]}
