from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func6_dict_http_query(query: Any) -> dict:
    result_data: dict = {}

    if not isinstance(query, str):
        raise Exception(["arg should be str"])

    if len(str(query)) > 0:
        data = str(query).split("&")
        for value in data:
            if value.find("=") != -1:
                tmp = value.split("=")
                if tmp[0] in result_data:
                    result_data[tmp[0]].append(tmp[1])
                else:
                    result_data[tmp[0]] = [tmp[1]]

    return result_data
