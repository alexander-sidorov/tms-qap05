import datetime
from typing import Any


def func4_oldest(d1: dict[Any, datetime]) -> dict:
    oldest = datetime.date.today()

    if not isinstance(d1, dict):
        return {"errors": ["should be dict"]}

    for key, value in d1.items():
        if not isinstance(value, (datetime.date, datetime.datetime)):
            return {"errors": ["args should be date"]}
        if value > oldest:
            return {"errors": ["is not born"]}

    result_data = min(d1, key=lambda name: d1[name])

    return {"data": result_data}
