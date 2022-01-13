from typing import Any


def func12_even_keys_odd_values(*args: Any) -> dict:
    result_data: dict[Any, Any] = {}
    odd_args = []
    even_args = []

    if len(args) % 2 == 1:
        return {"errors": ["should be even count"]}
    for key, arg in enumerate(args, start=1):
        if key % 2 == 1:
            odd_args.append(arg)
        else:
            even_args.append(arg)

    for index, value in enumerate(odd_args):
        if isinstance(value, (list, dict, set, frozenset)):
            return {"errors": ["Unhashable type: 'list'"]}

        result_data[value] = None
        if index < len(even_args):
            result_data[value] = even_args[index]

    if len(odd_args) < len(even_args):
        result_data[...] = even_args[
            len(odd_args) : len(even_args) + 1  # noqa: E203
        ]

    return {"data": result_data}
