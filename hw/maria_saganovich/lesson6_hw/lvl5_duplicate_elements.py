from typing import Any


def func5_duplicate_elements(collection: Any) -> dict:
    result_data: Any = {}
    counter: dict = {}

    if type(collection) not in [list, tuple, str]:
        return {"errors": "Not supported type"}

    for value in collection:
        if isinstance(value, list):
            return {"errors": "Unhashable type: 'list'"}

        counter[value] = counter.get(value, 0) + 1
        result_data = {
            data: count for data, count in counter.items() if count > 1
        }

    return {"data": result_data}
