from typing import Dict, Any
from datetime import datetime
from datetime import date


Result = Dict[str, Any]


def if_palindrome(u_input: str) -> Result:
    result: Result = {}
    if isinstance(u_input, str):
        u_input = u_input.lower()
        u_input = u_input.replace(" ", "")
        list1 = list2 = list(u_input)
        list2.reverse()
        if list1 == list2:
            result["data"] = ["This is a palindrome"]
        else:
            result["data"] = ["This is not a palindrome"]
    else:
        result["error"] = ["Input must be a string"]
    return result


print(if_palindrome("А муза рада музе без ума да разума"))
print(if_palindrome("b"))
print(if_palindrome(True))


def multiplication(*args: int) -> Result:
    result: Result = {}
    for item in args:
        if not isinstance(item, int):
            result["error"] = ["Input must be a number"]
        else:
            result["data"] = sum(args)
    return result


print(multiplication(1,2,3,8.7))
print(multiplication((1,2,3)))


def birthday(my_date: tuple) -> Result:
    result: Result = {}

    now = date.today()
    age = int((now - my_date).days)
    age = round(age / 365)

    return age


print(birthday(date(1993, 8, 3)))
