from typing import Any


def func1_palindrome(palindrome: Any) -> dict:
    result_data: bool = False

    if isinstance(palindrome, str):
        str_palindrome = palindrome
        if str_palindrome == str_palindrome[::-1]:
            result_data = True
        else:
            result_data = False

    return {"data": result_data}
