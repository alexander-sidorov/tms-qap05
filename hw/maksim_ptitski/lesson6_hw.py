import collections
from datetime import date
from typing import Any


def is_the_string_is_the_palindrome(string: str) -> dict:
    result = {}
    if not isinstance(string, str):
        return {"errors": "provided argument is not a string"}
    else:
        if string[:] == string[::-1]:
            result["data"] = True
        else:
            result["data"] = False
    return result


def data_multiplication(*any_data: Any) -> dict:
    result = {}
    if len(any_data) < 1:
        return {"errors": "must be more than 0 arguments"}
    elif len(any_data) == 1:
        result["data"] = any_data[0]
    else:
        mult_result = 1
        for i in any_data:
            mult_result *= i
            result["data"] = mult_result
    return result


def how_old_are_you(birthday: date) -> dict:
    result = {}
    today = date.today()
    if not isinstance(birthday, date):
        return {"errors": "wrong type of provided data"}
    if today.year < birthday.year:
        return {"errors": "you're not born yet"}
    else:
        result_age = today.year - birthday.year - 1
        if (
            birthday.month == today.month
            and birthday.day <= today.day  # noqa: W503
            or birthday.month < today.month  # noqa: W503
        ):
            result_age += 1

        result["data"] = {
            "year": birthday.year,
            "month": birthday.month,
            "day": birthday.day,
            "age": result_age,
        }
        return result


def the_oldest_one(birthday: dict) -> dict:
    if not isinstance(birthday, dict):
        return {"errors": "Given argument is not a dictionary"}
    else:
        name_result = ""
        temp = []
        for value in birthday.values():
            temp.append(value)
        min_t = min(temp)
        for keys, value in birthday.items():
            if value == min_t:
                name_result = keys
        return {"data": name_result}


def repeated_symbols(collection: Any) -> dict:
    types = (list, str, tuple)
    if type(collection) not in types:
        return {"errors": "given arguments are not a list, str or tuple"}
    else:
        dict_result: dict = collections.Counter(collection)
        result = {}
        result_dict = {}
        for key, value in dict_result.items():
            if value != 1:
                result_dict[key] = value
        result["data"] = result_dict
        return result
