from hw.siarhei_apanel.refakt import html_str


def test_html_str() -> None:
    result = html_str([])
    errors = result.get("errors")
<<<<<<< HEAD
=======
    assert isinstance(errors, list)
>>>>>>> main
    assert errors == sorted(errors)
