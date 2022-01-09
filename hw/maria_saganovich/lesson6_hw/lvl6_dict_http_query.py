from typing import Any


def func6_dict_http_query(query: Any) -> dict:  # noqa: CCR001
    result: dict[Any, Any] = {}
    is_error = False
    result_data: dict = {}
    result_error = []

    if type(query) != str:
        result_error.append("arg should be str")
        is_error = True
    else:
        if len(query) == 0:
            result_error.append("query is empty")
            is_error = True
        else:
            data = str(query).split("&")
            for value in data:
                if value.find("=") != -1:
                    tmp = value.split("=")
                    if tmp[0] in result_data.keys():  # noqa: SIM118
                        result_data[tmp[0]].append(tmp[1])
                    else:
                        result_data[tmp[0]] = [tmp[1]]
                else:
                    result_error.append("not query")
                    is_error = True

    if is_error:
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
