from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func1_palindrome(palindrome: Any) -> Any:
    assert isinstance(palindrome, str), ["Should be string"]

    return palindrome[:] == palindrome[::-1]
