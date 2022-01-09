from typing import Any


def func8_duplicate_char_number(arg: Any) -> dict:
    result: dict[Any, Any] = {}
    is_error = False
    result_data = ""
    result_error = []
    counter: dict = {}
    result_d = {}

    if type(arg) != str:
        result_error.append("arg should be str")
        is_error = True
    else:
        if len(arg) == 0:
            result_error.append("str is empty")
            is_error = True
        else:
            for value in arg:
                counter[value] = counter.get(value, 0) + 1
                result_d = {
                    data: count for data, count in counter.items() if count > 1
                }

            for key, value in result_d.items():
                result_data += key + str(value)

    if is_error:
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
