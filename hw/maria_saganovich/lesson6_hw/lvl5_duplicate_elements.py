from typing import Any


def func5_duplicate_elements(collection: Any) -> dict:
    result = {}
    is_error = False
    result_data: Any = []
    result_error = []
    counter: dict = {}

    if type(collection) != list:
        result_error.append("arg should be list")
        is_error = True
    else:
        if len(collection) == 0:
            result_error.append("list shouldn't be empty")
            is_error = True
        for value in collection:
            counter[value] = counter.get(value, 0) + 1
            result_data = {
                data: count for data, count in counter.items() if count > 1
            }

    if len(result_data) == 0:
        result_data = ["no duplicates"]

    if is_error:
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
