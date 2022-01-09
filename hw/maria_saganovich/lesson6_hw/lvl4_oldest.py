from datetime import date
from typing import Any


def func4_oldest(d1: Any) -> dict:  # noqa: CCR001
    result = {}
    oldest = date.today()
    is_error = False
    result_data = []
    error = []

    if type(d1) != dict:
        error.append("should be dict")
        is_error = True
    else:
        for key, value in d1.items():
            if isinstance(value, date):
                if value < oldest:
                    oldest = value
                    result_data = [key]
                elif value > oldest:
                    error.append("is not born")
                    is_error = True
                else:
                    result_data.append(key)
            else:
                error.append("args should be date")
                is_error = True

    if is_error:
        result["errors"] = sorted(error)
    else:
        result["data"] = sorted(result_data)

    return result
