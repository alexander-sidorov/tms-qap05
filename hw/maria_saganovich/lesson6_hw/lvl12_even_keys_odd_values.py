from typing import Any


def func12_even_keys_odd_values(*args: Any) -> dict:
    result: dict[Any, Any] = {}
    result_data: dict[Any, Any] = {}
    result_error = []
    odd_args = []
    even_args = []

    if len(args) % 2 == 1:
        result_error.append("should be even count")
    for key, arg in enumerate(args, start=1):
        if key % 2 == 1:
            odd_args.append(arg)
        else:
            even_args.append(arg)

    for index, value in enumerate(odd_args):
        if index < len(even_args):
            result_data[value] = even_args[index]
        else:
            result_data[value] = None

    if len(odd_args) < len(even_args):
        result_data[...] = even_args[
            len(odd_args) : len(even_args) + 1  # noqa: E203
        ]

    if bool(result_error):
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
