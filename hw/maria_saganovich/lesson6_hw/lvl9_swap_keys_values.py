from typing import Any


def func9_swap_keys_values(arg: Any) -> dict:
    result: dict[Any, Any] = {}
    is_error = False
    result_data: dict = {}
    result_error = []

    if type(arg) != dict:
        result_error.append("is not a dict")
        is_error = True
    else:
        if len(arg) == 0:
            result_error.append("dict is empty")
            is_error = True
        else:
            for key, value in arg.items():
                if value in result_data.keys():  # noqa: SIM118
                    result_data[value].append(key)
                else:
                    result_data[value] = [key]

    if is_error:
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
