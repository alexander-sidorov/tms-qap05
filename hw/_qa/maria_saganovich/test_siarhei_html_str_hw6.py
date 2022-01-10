from hw.siarhei_apanel.refakt import html_str


def test_html_str() -> None:
    assert html_str("") == {"errors": ["query is empty"]}
    assert html_str([]) == {"errors": ["arg should be str"]}
