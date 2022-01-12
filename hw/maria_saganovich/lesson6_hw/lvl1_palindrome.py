from typing import Any


def func1_palindrome(palindrome: Any) -> dict:
    result: dict[Any, Any] = {}
    result_data: bool = False
    result_error = []

    if type(palindrome) != str:
        result_error.append("should be str")
    else:
        str_palindrome = str(palindrome)
        if str_palindrome == str_palindrome[::-1]:
            result_data = True
        else:
            result_data = False

    if bool(result_error):
        result["errors"] = sorted(result_error)
    else:
        result["data"] = result_data

    return result