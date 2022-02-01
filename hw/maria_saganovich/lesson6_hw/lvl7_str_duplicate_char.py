import re
from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func7_str_duplicate_char(arg: Any) -> str:
    result = ""

    assert isinstance(arg, str), ["Invalid argument"]

    if len(arg) == 0:
        return result

    _tmp = re.split("(\\d+)", arg)
    _tmp = list(filter(None, _tmp))
    assert len(_tmp) > 1, ["Invalid string"]
    assert type(_tmp[0]) == str, ["Invalid string"]
    assert _tmp[1].isdigit(), ["Invalid string"]

    res = re.findall("([^\\d]+\\d+)", arg)
    for value in res:
        res2 = re.split("(\\d+)", value)
        result += res2[0] * int(res2[1])

    return result
