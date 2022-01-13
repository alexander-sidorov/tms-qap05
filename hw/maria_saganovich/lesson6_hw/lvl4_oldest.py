import datetime
from typing import Any


def func4_oldest(d1: Any) -> dict:
    oldest = datetime.datetime.today()
    result_data = []

    if not isinstance(d1, dict):
        return {"errors": ["should be dict"]}

    for key, value in d1.items():
        if not isinstance(value, (datetime.date, datetime.datetime)):
            return {"errors": ["args should be date"]}

        if isinstance(value, datetime.date):
            value = datetime.datetime(value.year, value.month, value.day)

        if value < oldest:
            oldest = value
            result_data = [key]
        elif value > oldest:
            return {"errors": ["is not born"]}
        else:
            result_data.append(key)

    return {"data": sorted(result_data)}
