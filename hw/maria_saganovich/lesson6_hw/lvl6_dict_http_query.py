from typing import Any


def func6_dict_http_query(query: Any) -> dict:
    result_data: dict = {}

    if not isinstance(query, str):
        return {"errors": ["arg should be str"]}

    if len(str(query)) > 0:
        data = str(query).split("&")
        for value in data:
            if value.find("=") != -1:
                tmp = value.split("=")
                if tmp[0] in result_data:
                    result_data[tmp[0]].append(tmp[1])
                else:
                    result_data[tmp[0]] = [tmp[1]]

    return {"data": result_data}
