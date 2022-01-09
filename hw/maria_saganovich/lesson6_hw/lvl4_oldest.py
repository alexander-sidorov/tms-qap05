from datetime import date
from typing import Any


def func4_oldest(d1: Any) -> dict:
    result = {}
    oldest = date.today()
    is_error = False
    result_data = []
    error = []

    if type(d1) != dict:
        error.append("should be dict")
        is_error = True
    else:
        for k, v in d1.items():
            if isinstance(v, date):
                if v < oldest:
                    oldest = v
                    result_data = [k]
                elif v > oldest:
                    error.append("is not born")
                    is_error = True
                else:
                    result_data.append(k)
            else:
                error.append("args should be date")
                is_error = True

    if is_error:
        result["errors"] = sorted(error)
    else:
        result["data"] = sorted(result_data)

    return result
