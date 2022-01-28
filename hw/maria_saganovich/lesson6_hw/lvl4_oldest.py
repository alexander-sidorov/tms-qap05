from datetime import date
from datetime import datetime
from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func4_oldest(d1: dict[Any, date]) -> dict:

    assert isinstance(d1, dict), ["should be dict"]
    assert len(d1) > 0, ["Empty Data"]

    for key, value in d1.items():
        assert isinstance(value, (date, datetime)), ["args should be date"]

        if isinstance(value, date):
            d1[key] = datetime(value.year, value.month, value.day, 0, 0, 0)

    return min(d1, key=lambda name: d1[name])
