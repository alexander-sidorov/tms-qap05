from typing import Any
from typing import Collection

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func5_duplicate_elements(elements: Any) -> dict:
    counter: dict = {}

    assert isinstance(elements, Collection), ["No Collections"]

    for value in elements:
        if isinstance(value, (list, dict, set, frozenset)):
            raise Exception(["Unhashable type: 'list'"])

        counter[value] = counter.get(value, 0) + 1

    return {data: count for data, count in counter.items() if count > 1}
