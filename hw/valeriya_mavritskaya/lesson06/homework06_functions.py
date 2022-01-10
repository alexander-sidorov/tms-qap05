import collections
import re
from datetime import date
from math import prod
from typing import Any


def if_palindrome_1(u_input: str) -> dict:
    result = {}
    if isinstance(u_input, str):
        u_input = u_input.lower()
        u_input = u_input.replace(" ", "")
        list1 = list(u_input)
        list2 = list(u_input)
        list2.reverse()
        if list1 == list2:
            result["data"] = "This is a palindrome"
        else:
            result["data"] = "This is not a palindrome"
    else:
        result["error"] = "Input must be a string"
    return result


def multiplication_2(*args: Any) -> dict:
    result = {}
    if any(
        type(item) not in [int, str, complex, float, list] for item in args
    ):
        result["error"] = "Input must be a number"
    else:
        result["data"] = prod(args)
    return result


def birthday_3(input_date: date) -> dict:
    result = {}
    now = date.today()
    if not isinstance(input_date, date):
        result["error"] = "Input must be a date"
    elif now > input_date:
        age = int((now - input_date).days)
        age = round(age / 365)
        result = {
            "year": input_date.year,
            "month": input_date.month,
            "day": input_date.day,
            "age": age,
        }
    else:
        result["error"] = "Date should be in the past"  # type: ignore
    return result


def oldest_4(people: dict) -> dict:
    result = {}
    if not isinstance(people, dict):
        result["error"] = "Input must be a dictionary"
    elif any(not isinstance(p, date) for p in people.values()):
        result["error"] = "Input must contain date"
    else:
        result["data"] = f"{min(people, key=people.get)}"  # type: ignore
    return result


def duplicates_5(collection: Any) -> dict:
    if (type(collection) not in [list, tuple, str]) or any(
        type(item) == dict for item in collection
    ):
        return {"error": "Invalid input"}
    result = {}
    select_duplicates = {i: collection.count(i) for i in collection}
    result["data"] = {
        key: value for (key, value) in select_duplicates.items() if value > 1
    }
    return result


def dict_from_http_6(input_query: str) -> dict:
    result: dict = {}
    if isinstance(input_query, str):
        pairs = input_query.split("&")
        for pair in pairs:
            parameter_and_value = pair.split("=")
            parameter = parameter_and_value[0]
            value = parameter_and_value[1]
            if parameter in result:
                result[parameter].append(value)
            else:
                result[parameter] = [value]
    else:
        return {"error": "Input must be http query"}
    return {"data": result}


def repeated_symbols_7(input_str: str) -> dict:
    if isinstance(input_str, str):
        groups = re.findall(r"(\D+\d+)", input_str)
        result = ""
        for element in groups:
            symbol = re.findall(r"\D+", element)[0]
            count = int(re.findall(r"\d+", element)[0])
            result = result + symbol * count
    else:
        return {"error": "Invalid input"}
    return {"data": result}


def count_amount_8(str_input: str) -> dict:
    if type(str_input) == str:
        result = {}
        count = collections.Counter(str_input)
        create_str = (f"{key}{value}" for (key, value) in count.items())
        result["data"] = "".join(create_str)
    else:
        return {"error": "Invalid input"}
    return result


def revert_dictionary_9(input_dictionary: dict) -> dict:
    if type(input_dictionary) != dict:
        return {"error": "Invalid input"}
    result: dict[int, list] = {}
    values_list = []
    for value in input_dictionary.values():
        values_list.append(value)
    for key, value in input_dictionary.items():
        if values_list.count(value) > 1:
            result.setdefault(value, []).append(key)
        else:
            result[value] = key
    return {"data": result}


def join_dictionary_10(keys: Any, values: Any) -> dict:
    dictionary_length = max(len(keys), len(values))
    result: dict = {}
    if dict in [type(keys), type(values)]:
        return {"error": "Invalid input"}
    for index in range(dictionary_length):
        should_use_source_key = len(keys) > index
        should_use_source_value = len(values) > index
        result_key = keys[index] if should_use_source_key else ...
        result[result_key] = (
            (values[index] if should_use_source_value else None)
            if should_use_source_key
            else [values[index]]
            if ... not in result
            else result[result_key] + [values[index]]
        )
    return {"data": result}


def set_operations_11(set1: set, set2: set) -> dict:
    if type(set1) != set or type(set2) != set:
        return {"error": "Input should be set"}
    result = {
        "a&b": set1 & set2,
        "a|b": set1 | set2,
        "a-b": set1 - set2,
        "b-a": set2 - set1,
        "|a-b|": set1 ^ set2,
        "a in b": set1.issubset(set2),
        "b in a": set2.issubset(set1),
    }
    return {"data": result}


def mk_dictionary_12(*args: Any) -> dict:
    if len(args) % 2 != 0:
        return {"error": "Use even number of elements"}
    result = {args[i]: args[i + 1] for i in range(0, len(args), 2)}
    return {"data": result}
