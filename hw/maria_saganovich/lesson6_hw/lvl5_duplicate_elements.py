from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func5_duplicate_elements(collection: Any) -> dict:
    counter: dict = {}

    if not isinstance(collection, (list, dict, tuple, str, set, range)):
        raise Exception(["Invalid collection type"])
    if len(collection) == 0:
        return {}

    for value in collection:
        if isinstance(value, (list, dict, set, frozenset)):
            raise Exception(["Unhashable type: 'list'"])

        counter[value] = counter.get(value, 0) + 1

    return {data: count for data, count in counter.items() if count > 1}
