from datetime import date
from datetime import datetime
from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func4_oldest(d1: dict[Any, date]) -> dict:
    oldest = datetime.today()

    if not isinstance(d1, dict):
        raise Exception(["should be dict"])

    for key, value in d1.items():
        if not isinstance(value, (date, datetime)):
            raise Exception(["args should be date"])
        if isinstance(value, date):
            d1[key] = datetime(value.year, value.month, value.day, 0, 0, 0)

        if d1[key] > oldest:
            raise Exception(["is not born"])

    return min(d1, key=lambda name: d1[name])
