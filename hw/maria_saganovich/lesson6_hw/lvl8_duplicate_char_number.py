from typing import Any


def func8_duplicate_char_number(arg: Any) -> dict:
    result_data = ""
    prev_val = ""
    pair_key = ""
    count = 0
    counter: dict = {}

    if not isinstance(arg, str):
        return {"errors": ["Invalid argument"]}

    for value in arg:
        if value.isdigit():
            return {"errors": ["Unsupported type 'int'"]}

        if prev_val != value:
            pair_key += value
            count = 0

        prev_val = value
        count += 1  # noqa: SIM113
        counter[pair_key] = {value: count}

    for _key, _value in counter.items():
        for key, value in _value.items():
            result_data += str(key) + str(value)

    return {"data": result_data}
