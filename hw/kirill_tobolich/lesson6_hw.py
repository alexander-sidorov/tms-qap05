import collections
from collections import Counter
from datetime import date
from typing import Any


def palindrome(string: str) -> dict:
    result = {}
    if not isinstance(string, str):
        return {"errors": "given argument is not string type"}
    if string[:] == string[::-1]:
        result["data"] = True
    else:
        result["data"] = False
    return result


def multiply(*args: Any) -> dict:
    result = {}
    try:
        if len(args) < 1:
            return {"errors": "no argument is given"}
        elif len(args) == 1:
            result["data"] = args[0]
        else:
            multiplication_result = 1
            for i in args:
                multiplication_result *= i
                result["data"] = multiplication_result
    except TypeError:
        return {"errors": "given arguments' types can't be multiplied"}
    return result


def get_formatted_birthday(birthday_date: date) -> dict:
    result = {}
    if not isinstance(birthday_date, date):
        return {"errors": "given argument is not object of date type"}
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


def get_the_eldest(dictionary: dict) -> dict:
    result = {}
    if not isinstance(dictionary, dict):
        return {"errors": "Given argument is not a dictionary"}
    keys = []
    values = []
    for key, value in dictionary.items():
        if not isinstance(value, date):
            return {"errors": "key value is not object of date type"}
        keys.append(key)
        values.append(value)
    min_age = min(values)
    name_of_min_age = keys[values.index(min_age)]
    result["data"] = name_of_min_age
    return result


def get_the_same_elements_in_collection(collection: Any) -> dict:
    types = (list, str, tuple)
    if type(collection) not in types:
        return {
            "errors": "given argument with keys is not a list, str or tuple"
        }
    result = {}
    try:
        counter: Counter = collections.Counter(collection)
    except TypeError:
        return {"errors": "collection contains unhashable type"}
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
        return {"errors": "given argument is not string type"}
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
        return {"errors": "given query contains wrong format"}
    result["data"] = dict_with_queries
    return result


def repeat_chars(string: str) -> dict:
    result = {}
    if not isinstance(string, str):
        return {"errors": "given argument is not string type"}
    elif len(string) % 2 != 0:
        return {"errors": "length of given string is odd"}
    elif not string[::2].isalpha() or not string[1::2].isdigit():
        return {"errors": "given string is in wrong format"}
    else:
        list_of_chars = list(filter(str.isalpha, string))
        list_of_digits = list(filter(str.isdigit, string))
        result_string = "".join(
            [
                char * int(digit)
                for char, digit in zip(list_of_chars, list_of_digits)
            ]
        )
    result["data"] = result_string
    return result


def count_chars(string: str) -> dict:
    result = {}
    if not isinstance(string, str):
        return {"errors": "given argument is not string type"}
    counter: Counter = Counter()
    for i in string:
        counter[i] += 1
    dict_result = dict(counter)
    result_string = ""
    for key, value in dict_result.items():
        char_and_counter = f"{key}{str(value)}"
        result_string += char_and_counter
    result["data"] = result_string
    return result


def inverted_dictionary(dictionary: dict) -> dict:
    result = {}
    if not isinstance(dictionary, dict):
        return {"errors": "given argument is not dict type"}
    inverted_dict = {}
    try:
        for key, value in dictionary.items():
            if value not in inverted_dict:
                inverted_dict[value] = [key]
            else:
                inverted_dict[value].append(key)
    except TypeError:
        return {"errors": "dictionary value contains unhashable type"}
    for new_key, new_value in inverted_dict.items():
        if len(new_value) < 2:
            inverted_dict[new_key] = new_value[0]
    result["data"] = inverted_dict
    return result


def zip_collections_to_dict(  # noqa: CCR001
    keys_collection: Any, values_collection: Any
) -> dict:
    result: dict = {}
    errors: list = []
    types = (list, str, tuple)
    if type(keys_collection) not in types:
        errors.append("given argument with keys is not a list, str or tuple")
    if type(values_collection) not in types:
        errors.append("given argument with values is not a list, str or tuple")
    if errors:
        result["errors"] = errors
    else:
        keys_collection = list(keys_collection)
        values_collection = list(values_collection)
        if len(keys_collection) > len(values_collection):
            differance = len(keys_collection) - len(values_collection)
            values_collection.extend(None for i in range(differance))
            list_of_zipped_collections = list(
                zip(keys_collection, values_collection)
            )
            try:
                result["data"] = dict(list_of_zipped_collections)
            except TypeError:
                return {
                    "errors": "collections contain values with unhashable type"
                }
        elif len(keys_collection) < len(values_collection):
            differance_list = values_collection[
                len(keys_collection) :  # noqa: E203
            ]  # noqa: E203
            list_with_the_same_length = values_collection[
                : len(keys_collection)  # noqa: E203
            ]
            list_of_zipped_collections = list(
                zip(keys_collection, list_with_the_same_length)
            )
            list_of_zipped_collections.append(("...", differance_list))
            try:
                result["data"] = dict(list_of_zipped_collections)
            except TypeError:
                return {
                    "errors": "collections contain values with unhashable type"
                }
        else:
            list_of_zipped_collections = list(
                zip(keys_collection, values_collection)
            )
            try:
                result["data"] = dict(list_of_zipped_collections)
            except TypeError:
                return {
                    "errors": "collections contain values with unhashable type"
                }
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
        return {"errors": "Quantity of given arguments is not even"}
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
            return {"errors": "odd argument is unhashable type"}
        result = {"data": dictionary_from_arguments}
    return result
