from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func11_relation_bt_2_sets(arg1: Any, arg2: Any) -> dict:
    assert isinstance(arg1, (frozenset, set)), ["arg1 should be set"]
    assert isinstance(arg2, (frozenset, set)), ["arg2 should be set"]

    return {
        "a&b": arg1 & arg2,
        "a|b": arg1 | arg2,
        "a-b": arg1 - arg2,
        "b-a": arg2 - arg1,
        "|a-b|": arg1 ^ arg2,
        "a in b": arg1.issubset(arg2),
        "b in a": arg2.issubset(arg1),
    }
