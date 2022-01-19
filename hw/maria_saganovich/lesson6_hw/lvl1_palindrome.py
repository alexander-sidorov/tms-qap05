from typing import Any

from hw.maria_saganovich.lesson6_hw.func_decorator import my_func_decorator


@my_func_decorator
def func1_palindrome(palindrome: Any) -> bool:
    result_data: bool = False

    if isinstance(palindrome, str):
        str_palindrome = palindrome
        if str_palindrome == str_palindrome[::-1]:
            result_data = True

    return result_data
