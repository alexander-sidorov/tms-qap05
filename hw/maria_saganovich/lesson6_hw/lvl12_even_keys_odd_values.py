# Функция принимает бесконечное количество позиционных аргументов.
# Из них она составляет и возвращает словарь. Словарь составляется по правилу:
# четные элементы - ключи, нечетные - значения, попарно.
#
# assert f(1,2) == {"data": {1: 2}}
from typing import Any


def func12_even_keys_odd_values(*args: Any) -> dict:
    result = {}
    is_error = False
    result_data = {}
    result_error = []
    odd_args = []
    even_args = []

    if not is_error:
        for arg in args:
            if type(arg) != int:
                result_error.append("should be number")
                is_error = True
            else:
                if arg % 2 == 1:
                    odd_args.append(arg)
                else:
                    even_args.append(arg)

        for index, value in enumerate(odd_args):
            if index < len(even_args):
                result_data[value] = even_args[index]
            else:
                result_data[value] = None

        if len(odd_args) < len(even_args):
            result_data[...] = even_args[len(odd_args) : len(even_args) + 1]

    if is_error:
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
