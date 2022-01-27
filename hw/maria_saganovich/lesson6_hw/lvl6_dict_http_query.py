from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func6_dict_http_query(query: Any) -> dict:
    result: dict = {}

    assert isinstance(query, str), ["arg should be str"]

    if len(query) < 2:
        return {}

    if "=" not in query:
        return {query: [""]}

    data = str(query).split("&")
    for value in data:
        if value.find("=") != -1:
            tmp = value.split("=")
            if tmp[0] in result:
                result[tmp[0]].append(tmp[1])
            else:
                result[tmp[0]] = [tmp[1]]

    return result
