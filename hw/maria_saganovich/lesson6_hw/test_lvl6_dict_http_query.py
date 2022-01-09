from hw.maria_saganovich.lesson6_hw.lvl6_dict_http_query import func6_dict_http_query


def test_func6_dict_http_query() -> None:
    assert func6_dict_http_query("x=1&x=2&y=3") == {"data": {"x": ["1", "2"], "y": ["3"]}}
    assert func6_dict_http_query("x=1&x=2&y=3&b=45&b=7") == {"data": {"x": ["1", "2"], "y": ["3"], "b": ["45", "7"]}}
    assert func6_dict_http_query("") == {"errors": ["query is empty"]}
    assert func6_dict_http_query("3q&ue=ry5") == {"errors": ["not query"]}
    assert func6_dict_http_query([]) == {"errors": ["arg should be str"]}
