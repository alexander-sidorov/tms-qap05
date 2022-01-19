import re
from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func7_str_duplicate_char(arg: Any) -> str:
    result_data = ""

    if not isinstance(arg, str):
        raise Exception(["Invalid argument"])

    res = re.findall("([^\\d]+\\d+)", arg)
    for value in res:
        res2 = re.split("(\\d+)", value)
        result_data += res2[0] * int(res2[1])

    return result_data
