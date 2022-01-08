from typing import Any


def func1_palindrome(palindrome: Any) -> dict:
    result = {"errors": Any}
    if type(palindrome) != str:
        result["errors"] = ["should be str"]
    else:
        b = palindrome.split()
        b = ''.join(b)
        str_palindrome = str(b).lower()
        if str_palindrome == str_palindrome[::-1]:
            result = {"data": True}
        else:
            result = {"data": False}

    return result
