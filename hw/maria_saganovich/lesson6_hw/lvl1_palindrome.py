from typing import Any


def func1_palindrome(palindrome: Any) -> dict:
    result = {"errors": Any}
    if type(palindrome) != str:
        result["errors"] = ["should be str"]
    else:
        b1 = palindrome.split()
        b1 = ''.join(b1)
        str_palindrome = str(b1).lower()
        if str_palindrome == str_palindrome[::-1]:
            result = {"data": True}
        else:
            result = {"data": False}

    return result
