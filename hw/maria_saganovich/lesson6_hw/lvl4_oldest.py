from datetime import date
from typing import Any


def func4_oldest(d1: Any) -> dict:
    result = {}
    oldest = date.today()
    result_data = []
    error = []

    if type(d1) != dict:
        return {"errors": ["should be dict"]}

    for key, value in d1.items():
        if not isinstance(value, date):
            error.append("args should be date")
        else:
            if value < oldest:
                oldest = value
                result_data = [key]
            elif value > oldest:
                error.append("is not born")
            else:
                result_data.append(key)

    if bool(error):
        result["errors"] = sorted(error)
    else:
        result["data"] = sorted(result_data)

    return result
