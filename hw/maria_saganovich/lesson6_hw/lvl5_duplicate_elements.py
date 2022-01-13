from typing import Any


def func5_duplicate_elements(collection: Any) -> dict:
    result_data: Any = {}
    counter: dict = {}

    if not isinstance(collection, (list, dict, tuple, str, set, range)):
        return {"errors": ["Invalid collection type"]}
    if len(collection) == 0:
        return {"data": result_data}

    for value in collection:
        if isinstance(value, (list, dict, set, frozenset)):
            return {"errors": ["Unhashable type: 'list'"]}

        counter[value] = counter.get(value, 0) + 1
        result_data = {
            data: count for data, count in counter.items() if count > 1
        }

    return {"data": result_data}
