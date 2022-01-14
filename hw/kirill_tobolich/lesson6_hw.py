import collections
import re
from collections import Counter
from datetime import date
from typing import Any


def palindrome(string: str) -> dict:
    result = {}
    if not isinstance(string, str):
        return {"errors": ["given argument is not string type"]}
    if string[:] == string[::-1]:
        result["data"] = True
    else:
        result["data"] = False
    return result


def multiply(*args: Any) -> dict:
    result = {}
    try:
        if len(args) < 1:
            return {"errors": ["no argument is given"]}
        elif len(args) == 1:
            result["data"] = args[0]
        else:
            multiplication_result = 1
            for i in args:
                multiplication_result *= i
                result["data"] = multiplication_result
    except TypeError:
        return {"errors": ["given arguments' types can't be multiplied"]}
    return result


def get_formatted_birthday(birthday_date: date) -> dict:
    result = {}
    if not isinstance(birthday_date, date):
        return {"errors": ["given argument is not object of date type"]}
    today = date.today()
    birthday_this_year = date(
        today.year, birthday_date.month, birthday_date.day
    )
    if birthday_this_year > today:
        age = today.year - birthday_date.year - 1
    else:
        age = today.year - birthday_date.year
    result["data"] = {
        "year": birthday_date.year,
        "month": birthday_date.month,
        "day": birthday_date.day,
        "age": age,
    }
    return result


def get_the_eldest(dictionary: dict[Any, date]) -> dict:
    result = {}
    if not isinstance(dictionary, dict):
        return {"errors": ["Given argument is not a dictionary"]}
    for _key, value in dictionary.items():
        if not isinstance(value, date):
            return {"errors": ["key value is not object of date type"]}
    min_value = min(dictionary, key=lambda v: dictionary[v])
    result["data"] = min_value
    return result


def get_the_same_elements_in_collection(collection: Any) -> dict:
    types = (list, str, tuple, set, dict)
    if type(collection) not in types:
        return {
            "errors": ["given argument with keys is not a list, str or tuple"]
        }
    result = {}
    try:
        counter: Counter = collections.Counter(collection)
    except TypeError:
        return {"errors": ["collection contains unhashable type"]}
    result_dict = {}
    for key, value in counter.items():
        if value == 1:
            continue
        else:
            result_dict[key] = value
    result["data"] = result_dict
    return result


def http_query_parser(query: str) -> dict:
    result = {}
    if not isinstance(query, str):
        return {"errors": ["given argument is not string type"]}
    dict_with_queries = {}
    try:
        split_query = query.split("&")
        for i in split_query:
            index_of_equals = i.index("=")
            name = i[:index_of_equals]
            if name not in dict_with_queries:
                dict_with_queries[name] = [
                    i[index_of_equals + 1 :]  # noqa: E203
                ]
            else:
                dict_with_queries[name].append(
                    i[index_of_equals + 1 :]  # noqa: E203
                )  # noqa: E203
    except IndexError and ValueError:
        return {"errors": ["given query contains wrong format"]}
    result["data"] = dict_with_queries
    return result


def repeat_chars(string: str) -> dict:
    result = {}
    if not isinstance(string, str):
        return {"errors": ["given argument is not string type"]}
    numbers = re.findall(r"\d+", string)
    chars = re.findall(r"\D", string)
    if len(numbers) != len(chars):
        return {"errors": ["wrong format of string"]}
    else:
        zipped_lists = list(zip(numbers, chars))
        result_str = ""
        for num, char in zipped_lists:
            result_str += char * int(num)
        result["data"] = result_str
    return result


def count_chars(string: str) -> dict:
    result = {}
    if not isinstance(string, str):
        return {"errors": ["given argument is not string type"]}
    if len(string) == 0:
        result["data"] = ""
        return result
    if len(string) == 1:
        result["data"] = f"{string[0]}1"
        return result
    result_str = ""
    counter: dict = {string[0]: 0}
    previous_value = string[0]
    for letter in string:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
            substring = f"{previous_value}{counter[previous_value]}"
            result_str += substring
            counter.pop(previous_value)
            previous_value = letter
    result_str += f"{list(counter.keys())[0]}{list(counter.values())[0]}"
    result["data"] = result_str
    return result


def inverted_dictionary(dictionary: dict) -> dict:
    result = {}
    if not isinstance(dictionary, dict):
        return {"errors": ["given argument is not dict type"]}
    inverted_dict = {}
    try:
        for key, value in dictionary.items():
            if value not in inverted_dict:
                inverted_dict[value] = [key]
            else:
                inverted_dict[value].append(key)
    except TypeError:
        return {"errors": ["dictionary value contains unhashable type"]}
    for new_key, new_value in inverted_dict.items():
        if len(new_value) < 2:
            inverted_dict[new_key] = new_value[0]
    result["data"] = inverted_dict
    return result


def zip_collections_to_dict(keys: Any, values: Any) -> dict:
    result: dict = {}
    errors: list = []
    types = (list, str, tuple)
    unhashable_types = (list, set, dict)
    error_txt1 = "given argument with keys is not a list, str or tuple"
    error_txt2 = "given argument with values is not a list, str or tuple"
    error_txt3 = ["collections contain values with unhashable type"]
    if type(keys) not in types:
        errors.append(error_txt1)
    if type(values) not in types:
        errors.append(error_txt2)
    if errors:
        result["errors"] = errors
    else:
        if any((isinstance(keys, unhashable_types) for x in keys)):
            return {"errors": error_txt3}
        keys = list(keys)
        values = list(values)
        if len(keys) > len(values):
            differance = len(keys) - len(values)
            values.extend(None for i in range(differance))
            list_of_zipped_collections = list(zip(keys, values))
            result["data"] = dict(list_of_zipped_collections)
        elif len(keys) < len(values):
            differance_list = values[len(keys) :]  # noqa: E203
            list_with_the_same_length = values[: len(keys)]
            list_of_zipped_collections = list(
                zip(keys, list_with_the_same_length)
            )
            list_of_zipped_collections.append(("...", differance_list))
            result["data"] = dict(list_of_zipped_collections)
        else:
            list_of_zipped_collections = list(zip(keys, values))
            result["data"] = dict(list_of_zipped_collections)
    return result


def relations_between_two_sets(set1: set, set2: set) -> dict:
    errors: list = []
    if not isinstance(set1, set):
        errors.append("given first argument is not set type")
    if not isinstance(set2, set):
        errors.append("given second argument is not set type")
    if errors:
        return {"errors": errors}
    return {
        "data": {
            "a&b": set1 & set2,
            "a|b": set1 | set2,
            "a-b": set1 - set2,
            "b-a": set2 - set1,
            "|a-b|": set1 ^ set2,
            "a in b": set1.issubset(set2),
            "b in a": set2.issubset(set1),
        }
    }


def make_dictionary(*args: Any) -> dict:
    result = {}
    dictionary_from_arguments = {}
    if len(args) % 2 != 0:
        return {"errors": ["Quantity of given arguments is not even"]}
    else:
        keys = []
        values = []
        for i in args:
            if args.index(i) % 2 == 0:
                keys.append(i)
            else:
                values.append(i)
        try:
            dictionary_from_arguments = dict(list(zip(keys, values)))
        except TypeError:
            return {"errors": ["odd argument is unhashable type"]}
        result = {"data": dictionary_from_arguments}
    return result
