# Функция создаёт словарь из двух последовательностей:
# первый аргумент — последовательность ключей, второй — последовательность значений.
# Для ключей, которым не нашлись значения, ставить значение None.
# Значения, которым не нашлось ключей, попадают в список в ключ ....
#
# assert f("abc", [1,2]) == {"data": {"a": 1, "b": 2, "c": None}}
# assert f("ab", [1,2,3]) == {"data": {"a": 1, "b": 2, ...: [3]}}
from typing import Any


def func10_empty_keys_values(arg1: Any, arg2: Any) -> dict:
    result = {}
    is_error = False
    result_data = {}
    result_error = []

    if type(arg1) != str:
        result_error.append("incorrect arg")
        is_error = True
    elif type(arg2) != list:
        result_error.append("incorrect arg")
        is_error = True
    else:
        if len(arg1) == 0 and len(arg2) == 0:
            result_error.append("is undefined")
            is_error = True
        else:
            if len(arg1) == 0:
                result_error.append("str is empty")
                is_error = True
            if len(arg2) == 0:
                result_error.append("list is empty")
                is_error = True

        if not is_error:
            for index, values in enumerate(list(arg1)):
                if index < len(arg2):
                    result_data[values] = arg2[index]
                else:
                    result_data[values] = None

            if len(arg1) < len(arg2):
                result_data[...] = arg2[len(arg1) : len(arg2) + 1]

    if is_error:
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result
